from django.shortcuts import render, get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Activity
from .serializers import ActivityCreateSerializer, ActivitySerializer



@api_view(['POST', 'GET'])
def activity_create_view(request, *args, **kwargs):
  if request.method == 'POST':
    data = request.data
    data['created_by'] = request.user.pk
    serializer = ActivityCreateSerializer(data=data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'GET':
    serializer = ActivityCreateSerializer()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def activity_details_view(request, id, creator=None, *args, **kwargs):
  activity = get_object_or_404(Activity, id=id)
  serializer = ActivitySerializer(activity) 
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def activity_list_view(request, proj_id, *args, **kwargs):
  activities = get_list_or_404(Project.objects.filter(project=proj_id))
  serializer = ActivitySerializer(activities, many=True) 
  return Response(serializer.data)

    
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

