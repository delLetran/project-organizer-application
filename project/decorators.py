from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render



def decorator_test(view):
  def wrapper(request, *args, **kwargs):
    print(request.user.id)
    if request.user.is_authenticated & request.user.id == 1:
      return view(request, *args, **kwargs)
    else:
      # return render(request, 'error/403_error.html', {"error": "user unauthorized"})
      return Response({}, status=status.HTTP_400_BAD_REQUEST)
  return wrapper

# def is_project_member(view):
#   def wrapper(request,  *args, **kwargs):
    
#     if request.user.joined_project
      
      