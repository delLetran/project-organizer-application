# from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from .models import Task
from project.models import Project
from activity.models import Activity
User = get_user_model()


class TaskTest(APITestCase):
  def setUp(self):
    self.client_1 = APIClient()
    self.client_2 = APIClient()
    self.invalid_project = {
      "name":"invalid_project"
    }
    self.existing_project = {
      "name": "Existing Project",
      "description": "Project Existing ",
      "status": 1,
      "project_type": 3
    }
    self.existing_activity = {
      "name": "Test activity 1",
      "status": 3,
      "project": 1 
    }
    self.existing_activity_2 = {
      "name": "Test activity 2",
      "status": 3,
      "project": 1 
    }
    self.existing_task = {
      "name": "Test task 1",
      "importance": 3,
      "activity": 1 
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
    self.test_user2 = User.objects.create_user(
      email='test_user2@gmail.com',
      username='testuser2',
      first_name='test',
      last_name='user1',
      password='@l03e1t1',
      is_active=True
    )
    self.client_1.login(email=self.test_user1.email, password='@l03e1t1')
    self.client_2.login(email=self.test_user2.email, password='@l03e1t1')
    self.existing_project_res = self.client_1.post(
      reverse('project:create'),
      self.existing_project,
      format='json'
    )
    self.existing_activty_res = self.client_1.post(
      reverse('activity:create'),
      self.existing_activity,
      format='json'
    )
    self.existing_activty_2_res = self.client_1.post(
      reverse('activity:create'),
      self.existing_activity_2,
      format='json'
    )
    self.existing_task_res =  self.client_1.post(
      reverse('task:create'),
      self.existing_task,
      format='json'
    )
    self.test_task = {
        "name": "Test task 2",
        "impotance": 3,
        "activity": 1
    }
    self.test_another_task = {
        "name": "Test task 2",
        "impotance": 3,
        "activity": 2
    }
    self.test_invalid_task = {
        "name": "",
        "impotance": 3,
        "activity": 1
    }
    self.test_update_task = {
        "name": "updated task",
        "impotance": 5,
        "activity": 1
    }

  '''
  coverage run --source='.' manage.py test task.tests.TaskTest
  coverage run --source='.' manage.py test task.tests.TaskTest.test_create_task_already_used_name_on_same_activity
  '''

  def test_delete_task_not_found(self): 
    response = self.client_1.delete(
      reverse('task:delete', kwargs={'id':500})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_delete_task(self): 
    response = self.client_1.delete(
      reverse('task:delete', kwargs={'id':1})
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_get_method(self): 
    response = self.client_1.get(
      reverse('task:delete', kwargs={'id':1})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_task_invalid(self): 
    response = self.client_1.put(
      reverse('task:update', kwargs={'id':1}),
      self.test_invalid_task,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_update_task(self): 
    response = self.client_1.put(
      reverse('task:update', kwargs={'id':1}),
      self.test_update_task,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_get_method(self): 
    response = self.client_1.get(
      reverse('task:update', kwargs={'id':1})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_create_task_used_name_on_another_activity(self): 
    response = self.client_1.post(
      reverse('task:create'),
      self.test_task,
      format='json'
    )
    response = self.client_1.post(
      reverse('task:create'),
      self.test_another_task,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_create_task_already_used_name_on_same_activity_invalid(self): 
    response = self.client_1.post(
      reverse('task:create'),
      self.test_task,
      format='json'
    )
    response = self.client_1.post(
      reverse('task:create'),
      self.test_task,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_invalid_task(self): 
    response = self.client_1.post(
      reverse('task:create'),
      self.test_invalid_task,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_task(self): 
    response = self.client_1.post(
      reverse('task:create'),
      self.test_task,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_create_get_method(self): 
    response = self.client_1.get(reverse('task:create'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_task_list(self): 
    response = self.client_1.get(
      reverse('task:list', kwargs={'activity_id':1})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_task_details(self): 
    response = self.client_1.get( 
      reverse('task:details', kwargs={'id':1})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
