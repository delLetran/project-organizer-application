# from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from project.models import Project
from .models import Activity
from task.models import Task
User = get_user_model()


class ActivityTest(APITestCase):
  def setUp(self):
    self.client = APIClient()
    self.invalid_project = {
      "name":"invalid_project"
    }
    self.existing_project = {
      "name": "Existing Project",
      "description": "Project Existing ",
      "status": 1,
      "project_type": 3
    }
    self.existing_project_2 = {
      "name": "Existing Project",
      "description": "Project Existing ",
      "status": 1,
      "project_type": 3
    }
    self.existing_activity = {
      "name": "Existing activity",
      "status": 3,
      "project": 1
    }
    self.existing_activity_2 = {
      "name": "Existing activity 2",
      "status": 3,
      "project": 1
    }
    self.test_user1 = User.objects.create_user(
      email='test_user1@gmail.com',
      username='testuser1',
      first_name='test',
      last_name='user1',
      password='@l03e1t1',
      is_staff=True,
      is_active=True
    )
    self.client.login(email=self.test_user1.email, password='@l03e1t1')
    # self.test_user2 = User.objects.create_user(
    #   email='test_user2@gmail.com',
    #   username='testuser2',
    #   first_name='test',
    #   last_name='user1',
    #   password='@l03e1t1',
    #   is_active=True
    # )
    self.existing_project_res = self.client.post(
      reverse('project:create'),
      self.existing_project,
      format='json'
    )
    self.existing_project_2_res = self.client.post(
      reverse('project:create'),
      self.existing_project_2,
      format='json'
    )
    self.existing_activty_res = self.client.post(
      reverse('activity:create'),
      self.existing_activity,
      format='json'
    )
    self.existing_activty_2_res = self.client.post(
      reverse('activity:create'),
      self.existing_activity_2,
      format='json'
    )
    self.project_instance = Project.objects.get(pk=1)
    self.test_activity1= {
        "name": "Test project 1",
        "status": 3,
        "project": self.project_instance.id
    }
    self.test_invalid_activity= {
        "name": "",
        "status": 3
    }
    self.test_existing_activity = {
      "name": "Existing activity",
      "status": 2,
      "project": 1 
    }
    self.test_update_activity = {
      "name": "Updated activity",
      "status": 2,
      "project": 1 
    }


  '''
  coverage run --source='.' manage.py test activity.tests.ActivityTest.test_list_activity
  '''
    
  def test_delete_activity(self): 
    response = self.client.delete(reverse('activity:delete', kwargs={'id':1}))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    response = self.client.get(reverse('activity:detail', kwargs={'id':1}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_delete_get_method(self): 
    response = self.client.get(reverse('activity:delete', kwargs={'id':1} ))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_update_invalid_activity(self): 
    response = self.client.put(
      reverse('activity:update', kwargs={'id':1}),
      self.test_invalid_activity,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_update_activity(self): 
    response = self.client.put(
      reverse('activity:update', kwargs={'id':1}),
      self.test_update_activity,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
  def test_update_get_method(self): 
    response = self.client.get(reverse('activity:update', kwargs={'id':1} ))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_create_invalid_activity(self): 
    response = self.client.post(
      reverse('activity:create'),
      self.test_invalid_activity,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_existing_activity(self): 
    response = self.client.post(
      reverse('activity:create'),
      self.test_existing_activity,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_activity(self): 
    response = self.client.post(
      reverse('activity:create'),
      self.test_activity1,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_create_get_method(self): 
    response = self.client.get(reverse('activity:create'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_details_activity(self): 
    response = self.client.get(reverse('activity:detail', kwargs={'id':1}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_list_activity_not_found_project(self): 
    response = self.client.get(reverse('activity:list', kwargs={'project_id':500}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_list_activity(self): 
    project_instance = Project.objects.get(pk=1)
    response = self.client.get(reverse('activity:list', kwargs={'project_id':project_instance.id}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
