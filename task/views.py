from django.shortcuts import render, get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from task.models import Task
from .serializers import TaskSerializer
from .serializers import TaskCreateSerializer
from .serializers import TaskUpdateSerializer



@api_view(['GET'])
def task_list_view(request, activity_id, *args, **kwargs):
  tasks = get_list_or_404(Task, activity=activity_id)
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def task_details_view(request, id, *args, **kwargs):
  task = get_object_or_404(Task, id=id)
  serializer = TaskSerializer(task)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def task_create_view(request, *args, **kwargs):
  if request.method == 'POST':
    data = request.data
    data['created_by'] = request.user.pk
    serializer = TaskCreateSerializer(data=data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  if request.method == 'GET':
    serializer = TaskCreateSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET'])
def task_update_view(request, id, *args, **kwargs):
  task_instance = get_object_or_404(Task, id=id)
  
  if request.method == 'PUT':
    serializer = TaskUpdateSerializer(data=request.data, instance=task_instance)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE', 'GET'])
def task_delete_view(request, id, *args, **kwargs):
  task_instance = get_object_or_404(Task, id=id)
  
  if request.method == 'DELETE':
    task_instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  if request.method == 'GET':
    serializer = TaskSerializer(task_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def project_details_view(request, slug, creator=None, *args, **kwargs):
#   project = get_object_or_404(Project, slug=slug)
#   serializer = ProjectSerializer(project) 
#   return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def project_list_view(request, *args, **kwargs):
#   projects = get_list_or_404(Project.objects.filter(created_by=request.user))
#   serializer = ProjectSerializer(projects, many=True) 
#   return Response(serializer.data)

    
# @api_view(['GET', 'UPDATE'])
# def project_update_view(request, slug, *args, **kwargs):
#   if request.method == 'UPDATE':
#     return Response({'test':'UPDATE'}, status=status.HTTP_200_OK)

#   if request.method == 'GET':
#     return Response({'test':'GET'}, status=status.HTTP_200_OK)
    

# @api_view(['GET', 'DELETE'])
# def project_delete_view(request, slug, *args, **kwargs):
#   if request.method == 'DELETE':
#     return Response({'test':'DELETE'}, status=status.HTTP_200_OK)

#   if request.method == 'GET':
#     return Response({'test':'GET'}, status=status.HTTP_200_OK)

