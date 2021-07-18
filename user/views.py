from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
# from rest_framework.decorators import permission_classes, 
# from rest_framework.decorators import authentication_classes
from core.utils import sendAsycnMail
from .tokens import create_token, get_user_token, is_user_token_expired
from .forms import SignUpForm
from .serializers import (
  OwnerSerializer, 
  UserSerializer,
  UserUpdateSerializer,
  ChangePasswordSerializer
)
User = get_user_model()

@api_view(['GET'])
def user_details_view(request, username, *args, **kwargs):
  profile = get_object_or_404(User, username=username)
  if User.objects.is_owner(request, username):
    serializer = OwnerSerializer(profile)
  else:
    serializer = UserSerializer(profile)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST','GET'])
def user_signup_view(request, *args, **kwargs):
  if request.method == 'POST':
    form = SignUpForm(request.data)
    if form.is_valid():
      user = form.save(commit=False)
      form.data['is_active']=False
      form.save()
      token = create_token(user)
      task_id = sendAsycnMail(
        # form.data['username'], 
        form.data['email'],
        token
      )
      return Response(form.data, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'GET':
    form = SignUpForm()
    return Response(form.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def user_activate_view(request, uid, token):
  decoded_id = force_text(urlsafe_base64_decode(uid))
  user = get_object_or_404(User, pk=decoded_id)
  user_token = get_user_token(user)
  context = {
    'message':"",
    'error': None
  }
  if user_token == token:
    if not is_user_token_expired(user): 
      user.is_active=True
      user.save()
      context['message'] = f'Email verified, Account {user.username} activated'
      return Response(context, status=status.HTTP_200_OK)
    # else:
    #   context['error'] = 'Activation link has expired. resend an email verification'
  # else:
  context['error'] = 'Email verification fail.'
  return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_resend_email_verification_view(request, *args, **kwargs):
  user = request.user
  token = create_token(user)
  sendAsycnMail(
    user.email,
    token
  )
  return Response({'message':f'Account activation was sent to your email'}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT']) 
def user_update_view(request, *args, **kwargs):
  user = get_object_or_404(User, username=request.user)
  if request.method == 'GET':
    serializer = UserUpdateSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  if request.method == 'PUT':
    serializer = UserUpdateSerializer(data=request.data, instance=user)
    if serializer.is_valid():
      serializer.save()
      user = get_object_or_404(User, username=serializer.instance)
      serializer = OwnerSerializer(user)
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT']) 
def user_update_password_view(request, *args, **kwargs):
  if request.method == 'GET':
    serializer = ChangePasswordSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)
  if request.method == 'PUT':
    serializer = ChangePasswordSerializer(data=request.data, instance=request.user)
    if serializer.is_valid(raise_exception=True):
      user = serializer.save()
    # if using drf authtoken, create a new token 
    return Response({'token': 'token.key'}, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def user_delete_view(request, *args, **kwargs):
  user = get_object_or_404(User, username=request.user)
  if request.method == 'GET':
    serializer = OwnerSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  if request.method == 'DELETE':
    user.delete() 
    return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def user_confirm_delete_view(request, *args, **kwargs):
#   user = get_object_or_404(Profile, username=request.user)
#   if request.method == 'POST':
#     #check Credentials
#     username = request.data['username']
#     password = request.data['password']
#     user.delete() 
#     return Response(status=status.HTTP_204_NO_CONTENT)