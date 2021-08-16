from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# from core.utils import is_str
from .models import Collaborator
from project.models import Project
User = get_user_model()
from .serializers import CollaboratorSerializer
from .serializers import CollaboratorUpdateSerializer
from .serializers import CollaboratorCreateSerializer
import json



@api_view(['PUT', 'GET'])
def update_collaborator_position_view(request, collaborator_id, *args, **kwargs):
  data = request.data
  # data = json.dumps(request.data)
  collaborator_instance = get_object_or_404(Collaborator, id=collaborator_id) 
  if request.method == 'PUT':
    serializer = CollaboratorUpdateSerializer(data=data, instance=collaborator_instance)
    if serializer.is_valid():
      serializer.save()
      instance = get_object_or_404(Collaborator, id=collaborator_id)
      serializer = CollaboratorSerializer(instance)
      return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET': 
    serializer = CollaboratorSerializer(collaborator_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_project_collaborators_view(request, project_id, *args, **kwargs):
  colaborators = get_list_or_404(Collaborator, project=project_id) 
  if request.method == 'GET':
    serializer = CollaboratorSerializer(colaborators, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def invite_view(request, invitee, project_id, position="Member", *args, **kwargs):
  data = {}
  if request.method == 'POST':
    _receiver = get_object_or_404(User, username=invitee)
    _project = get_object_or_404(Project, id=project_id) 
    data['name'] = _receiver.pk
    data['project'] = _project.id
    data['inviter'] = request.user.pk
    data['position'] = position
    serializer = CollaboratorCreateSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      instance = get_object_or_404(Collaborator, name=_receiver.pk, project=_project.id)
      serializer = CollaboratorSerializer(instance)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    serializer = CollaboratorCreateSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT', 'GET'])
def accept_invite_view(request, project_id, *args, **kwargs):
  user = request.user
  invite_instance = get_object_or_404(Collaborator, project=project_id, name=user) 
  if request.method == 'PUT':
    invite_status = invite_instance.accept_collaboration_invite()
    return Response(status=status.HTTP_204_NO_CONTENT)
    # return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)

  if request.method == 'GET': 
    serializer = CollaboratorSerializer(invite_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
# auth (project admin only view)
# @api_view(['PUT', 'GET'])
# position_change_view for joined collaborator(request, invitee, project_id, *args, **kwargs):
  # data = request.data


@api_view(['PUT', 'GET'])
def decline_invite_view(request, project_id, *args, **kwargs):
  user = request.user
  invite_instance = get_object_or_404(Collaborator, project=project_id, name=user) 
  if request.method == 'PUT':
    invite_status = invite_instance.decline_collaboration_invite()
    return Response(status=status.HTTP_204_NO_CONTENT)
    # return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)

  if request.method == 'GET':
    serializer = CollaboratorSerializer(invite_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET'])
def leave_project_view(request, project_id, *args, **kwargs):
  user = request.user
  invite_instance = get_object_or_404(Collaborator, project=project_id, name=user) 
  if request.method == 'PUT':
    invite_status = invite_instance.leave_project()
    return Response(status=status.HTTP_204_NO_CONTENT)
    # return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)

  if request.method == 'GET':
    serializer = CollaboratorSerializer(invite_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET'])
def remove_collaborator_view(request, collaborator, project_id, *args, **kwargs):
  user = request.user
  _collaborator = get_object_or_404(User, username=collaborator)
  invite_instance = get_object_or_404(Collaborator, project=project_id, name=_collaborator) 
  serializer = CollaboratorSerializer(invite_instance)
  print(serializer.data)
  if request.method == 'PUT':
    invite_status = invite_instance.remove_collaborator()
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
   
    # return Response(status=status.HTTP_204_NO_CONTENT)

  if request.method == 'GET':
    serializer = CollaboratorSerializer(invite_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

  

@api_view(['PUT', 'GET'])
def cancel_invite_view(request, invitee, project_id, *args, **kwargs):
  user = request.user
  _invitee = get_object_or_404(User, username=invitee)
  invite_instance = get_object_or_404(Collaborator, project=project_id, name=_invitee) 
  if request.method == 'PUT':
    invite_status = invite_instance.cancel_collaboration_invite()
    return Response({'status':invite_status}, status=status.HTTP_204_NO_CONTENT)

  if request.method == 'GET':
    serializer = CollaboratorSerializer(invite_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sent_invites_view(request,  *args, **kwargs):
  invites = get_list_or_404(Collaborator, inviter=request.user) 
  if request.method == 'GET':
    serializer = CollaboratorSerializer(invites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def received_invites_view(request, *args, **kwargs):
  invites = get_list_or_404(Collaborator, name=request.user)
  if request.method == 'GET':
    serializer = CollaboratorSerializer(invites, many=True)    
    return Response(serializer.data, status=status.HTTP_200_OK)
