from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import logout

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer
from .decorators import decorator_test



# decoded_id = force_text(urlsafe_base64_decode(uid))


  # add permission: project member, permission_type, creator
@api_view(['GET'])
@decorator_test
def project_details_view(request, slug, creator=None, *args, **kwargs):
  project = get_object_or_404(Project, slug=slug)
  serializer = ProjectSerializer(project) 
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def project_list_view(request, *args, **kwargs):
  projects = get_list_or_404(Project.objects.filter(created_by=request.user))
  serializer = ProjectSerializer(projects, many=True) 
  return Response(serializer.data)

@api_view(['POST', 'GET'])
def project_create_view(request, *args, **kwargs):
  if request.method == 'POST':
    data = request.data
    data['created_by'] = request.user.pk
    serializer = ProjectCreateSerializer(data=data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    serializer = ProjectCreateSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)

    
@api_view(['GET', 'UPDATE'])
def project_update_view(request, slug, *args, **kwargs):
  if request.method == 'UPDATE':
    return Response({'test':'UPDATE'}, status=status.HTTP_200_OK)

  if request.method == 'GET':
    return Response({'test':'GET'}, status=status.HTTP_200_OK)
    

@api_view(['GET', 'DELETE'])
def project_delete_view(request, slug, *args, **kwargs):
  if request.method == 'DELETE':
    return Response({'test':'DELETE'}, status=status.HTTP_200_OK)

  if request.method == 'GET':
    return Response({'test':'GET'}, status=status.HTTP_200_OK)



    