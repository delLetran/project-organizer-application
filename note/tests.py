# # from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model

# from rest_framework.test import APIClient, APITestCase
# from rest_framework import status
# import json

# from .models import Note
# from project.models import Project
# User = get_user_model()


# class ActvityTest(APITestCase):
#   def setUp(self):
#     self.client = APIClient()
#     self.invalid_project = {
#       "name":"invalid_project"
#     }
#     self.existing_project = {
#       "name": "Existing Project",
#       "description": "Project Existing ",
#       "status": 1,
#       "project_type": 3
#     }
#     self.existing_activity = {
#       "name": "Test project 1",
#       "status": 3,
#       "project": 1 
#     }
#     self.test_user1 = User.objects.create_user(
#       email='test_user1@gmail.com',
#       username='testuser1',
#       first_name='test',
#       last_name='user1',
#       password='@l03e1t1',
#       is_staff=True,
#       is_active=True
#     )
#     self.test_user2 = User.objects.create_user(
#       email='test_user2@gmail.com',
#       username='testuser2',
#       first_name='test',
#       last_name='user1',
#       password='@l03e1t1',
#       is_active=True
#     )
#     self.client.login(email=self.test_user1.email, password='@l03e1t1')
#     self.existing_project_res = self.client.post(
#       reverse('project-create'),
#       self.existing_project,
#       format='json'
#     )
    
#     self.existing_activty_res = self.client.post(
#       reverse('activity-create'),
#       self.existing_activity,
#       format='json'
#     )

#     project_instance = Project.objects.get(pk=1)
#     self.test_activity1= {
#         "name": "Test project 1",
#         "status": 3,
#         "project": project_instance.id
#     }
#     self.test_invalid_activity= {
#         "name": "",
#         "status": 3
#     }
#   def test_create_activity(self): 
#     response = self.client.post(
#       reverse('activity-create'),
#       self.test_activity1,
#       format='json'
#     )
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
#   def test_create_invalid_activity(self): 
#     response = self.client.post(
#       reverse('activity-create'),
#       self.test_invalid_activity,
#       format='json'
#     )
#     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#   def test_create_get_method(self): 
#     response = self.client.get(reverse('activity-create'))
#     self.assertEqual(response.status_code, status.HTTP_200_OK)




