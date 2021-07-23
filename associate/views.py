from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.decorators import permission_classes
# from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Associate
# from .forms import SignUpForm, UserUpdateForm
from .serializers import UserSerializer
from .serializers import AssociateSerializer
from .serializers import PeerCreateSerializer




@api_view(['POST', 'GET'])
def associate_invite_view(request, *args, **kwargs):
  if request.method == 'POST':
    data = request.data
    data['sender'] = request.user.pk
    if type(data['receiver']) == str:
      profile = get_object_or_404(User, username=data['receiver']) 
      data['receiver'] = profile.pk
    serializer = PeerCreateSerializer(data=data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    serializer = PeerCreateSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET'])
def user_accept_associate_view(request, username, *args, **kwargs):
  user = request.user
  sender = get_object_or_404(User, username=username)
  invite = get_object_or_404(Associate, sender=sender, receiver=user) 
  is_accepted = invite.accept_peer_invite()
  if is_accepted:
    return Response({'invite_accepted':is_accepted}, status=status.HTTP_200_OK)
  return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def user_associates_list_view(request, *args, **kwargs):
  associates_list = []
  user = request.user 
  for associate in user.get_associates():
    associate_serializer = AssociateSerializer(associate, many=True)
    associates_list.append(associate_serializer)
  return Response(associates_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_mutual_associates_list_view(request, *args, **kwargs):
  mutuals_list = request.user.get_associate_with_mutual_associates_list()
  mutual_associates_list = []
  for (profile, assocs) in mutuals_list:
    profile_serializer = UserSerializer(profile)
    assocs_serializer = AssociateSerializer(assocs, many=True)
    data = {
      'profile': profile_serializer.data,
      'mutual_associates': assocs_serializer.data
    }
    mutual_associates_list.append(data)
  return Response(mutual_associates_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_mutual_associates_detail_view(request, username, *args, **kwargs):
  user = request.user
  profile = get_object_or_404(User, username=username)
  
  if not User.objects.is_owner(request, username):
    mutual_assocs = user.get_mutual_associates_details(profile)
    print(mutual_assocs)
    serializer = AssociateSerializer(mutual_assocs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(status=status.HTTP_204_NO_CONTENT)


