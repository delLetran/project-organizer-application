from django.shortcuts import get_object_or_404, get_list_or_404
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

from core.utils import is_str
from .models import Associate
# from .forms import SignUpForm, UserUpdateForm
from .serializers import UserSerializer
from .serializers import AssociateSerializer
from .serializers import ReceivedInviteSerializer
from .serializers import SentInviteSerializer
from .serializers import PeerUpdateSerializer
from .serializers import PeerCreateSerializer




@api_view(['POST', 'GET'])
def invite_view(request, invitee, *args, **kwargs):
  data = {}
  if request.method == 'POST':
    data['sender'] = request.user.pk
    _receiver = get_object_or_404(User, username=invitee) 
    data['receiver'] = _receiver.pk
    serializer = PeerCreateSerializer(data=data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    serializer = PeerCreateSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET'])
def accept_invite_view(request, inviter, *args, **kwargs):
  invite_instance = None
  try:
    sender = get_object_or_404(User, username=inviter) 
    invite_instance = get_object_or_404(Associate, sender=sender, receiver=request.user)  
  except:
    pass
    
  if request.method == 'PUT':
    if not invite_instance == None:
      invite_status = invite_instance.accept_peer_invite()
      return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    if not invite_instance == None:
      serializer = ReceivedInviteSerializer(invite_instance)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT', 'GET'])
def decline_invite_view(request, inviter, *args, **kwargs):
  invite_instance = None
  try:
    sender = get_object_or_404(User, username=inviter) 
    invite_instance = get_object_or_404(Associate, sender=sender, receiver=request.user)  
  except:
    pass
    
  if request.method == 'PUT':
    if not invite_instance == None:
      invite_status = invite_instance.decline_peer_invite()
      return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    if not invite_instance == None:
      serializer = ReceivedInviteSerializer(invite_instance)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT', 'GET'])
def dissociate_view(request, associate, *args, **kwargs):
  associate_instance = None
  try:
    _associate = get_object_or_404(User, username=associate) 
    associate_instance = get_object_or_404(Associate, sender=_associate.pk, receiver=request.user)
  except:
    pass
  try:
    _associate = get_object_or_404(User, username=associate) 
    associate_instance = get_object_or_404(Associate, sender=request.user, receiver=_associate.pk)
  except:
    pass
  
  if request.method == 'PUT':
    if not associate_instance == None and associate_instance.status == "Accepted":
      associate_status = associate_instance.dissociate_peer()
      return Response({'status':associate_status}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'User not in associate list'}, status=status.HTTP_404_NOT_FOUND)
      
  if request.method == 'GET':
    if not associate_instance == None:
      serializer = AssociateSerializer(associate_instance)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
 

@api_view(['PUT', 'GET'])
def cancel_invite_view(request, invitee, *args, **kwargs):
  invite_instance = None
  try:
    receiver = get_object_or_404(User, username=invitee) 
    invite_instance = get_object_or_404(Associate, sender=request.user, receiver=receiver)  
  except:
    pass
  # print(invite_instance)
  if request.method == 'PUT':
    if not invite_instance == None and invite_instance.status == "Waiting":
      invite_status = invite_instance.cancel_peer_invite()
      return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'User not in waiting list'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    if not invite_instance == None:
      serializer = SentInviteSerializer(invite_instance)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def sent_invites_view(request, *args, **kwargs):
  invites = get_list_or_404(Associate, sender=request.user)
  if request.method == 'GET':
    serializer = SentInviteSerializer(invites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def received_invites_view(request, *args, **kwargs):
  invites = get_list_or_404(Associate, receiver=request.user)
  if request.method == 'GET':
    serializer = ReceivedInviteSerializer(invites, many=True)    
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def list_view(request, *args, **kwargs):
  associates_list = []
  user = request.user 
  for associate in user.get_associates():
    associate_serializer = UserSerializer(associate)
    associates_list.append(associate_serializer.data)
  return Response(associates_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def mutual_list_view(request, *args, **kwargs):
  mutuals_list = request.user.get_associate_with_mutual_associates_list()
  mutual_associates_list = []
  for (profile, assocs) in mutuals_list:
    profile_serializer = UserSerializer(profile)
    assocs_serializer = UserSerializer(assocs, many=True)
    data = {
      'profile': profile_serializer.data,
      'mutual_associates': assocs_serializer.data
    }
    mutual_associates_list.append(data)
  return Response(mutual_associates_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_mutual_list_view(request, username, *args, **kwargs):
  user = request.user
  profile = get_object_or_404(User, username=username)
  
  if not User.objects.is_owner(request, username):
    mutual_assocs = user.get_mutual_associates_details(profile)
    serializer = UserSerializer(mutual_assocs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def mutual_detail_view(request, username, *args, **kwargs):
#   user = request.user
#   profile = get_object_or_404(User, username=username)
  
#   if not User.objects.is_owner(request, username):
#     mutual_assocs = user.get_mutual_associates_details(profile)
#     print(mutual_assocs)
#     serializer = UserSerializer(mutual_assocs, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#   return Response(status=status.HTTP_204_NO_CONTENT)


