# from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from .models import Project

User = get_user_model()
from collaborator.models import Collaborator


class ProjectTest(APITestCase):
  def setUp(self):
    self.client_1 = APIClient()
    self.client_2 = APIClient()
    self.invalid_project = {
      "name":"invalid_project"
    }
    self.test_project_1 = {
      "name": "Test project 1",
      "description": "Project test 1",
      "status": 1,
      "project_type": 3
    }
    self.test_project_2 = {
      "name": "Test project 2",
      "description": "Project test 2",
      "status": 2,
      "project_type": 2
    }
    self.test_project_3 = {
      "name": "Test project 3",
      "description": "Project test 3",
      "created_by": 3,
      "status": 1,
      "project_type": 3
    }
    self.test_project_4 = {
      "name": "Test project 4 ",
      "description": "Project test 4",
      "created_by": 3,
      "status": 1,
      "project_type": 3
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

    self.project_1 = self.client_1.post(
      reverse('project:create'),
      self.test_project_1,
      format='json'
    )
    self.project_2 = self.client_1.post(
      reverse('project:create'),
      self.test_project_2,
      format='json'
    )
    self.project_3 = self.client_1.post(
      reverse('project:create'),
      self.test_project_3,
      format='json'
    )
    self.project_4 = self.client_2.post(
      reverse('project:create'),
      self.test_project_4,
      format='json'
    )

    self.test_new_project_1 = {
      "name": "Test new project 1",
      "description": "New project",
      "project_type": 3
    }
    self.test_project_invalid_project_type = {
      "name": "Test project invalid type",
      "description": "New project",
      "project_type": 500
    }
    self.test_project_invalid_status = {
      "name": "Test project invalid type",
      "description": "New project",
      "status": 500
    }
    self.test_update = {
      "name": "Test project 1 updated",
      "description": "Project testing updated",
      "status": 1,
      "project_type": 3
    }
    self.test_update_same_data = {
      "name": "Test project 1",
      "description": "Project testing ",
      "status": 1,
      "project_type": 3
    }
    self.test_update_existing_name = {
      "name": "Test project 2",
      "description": "Project testing ",
      "status": 1,
      "project_type": 3
    }


  ''' 
    coverage run --source='.' manage.py test project.tests.ProjectTest
    coverage run --source='.' manage.py test project.tests.ProjectTest.test_create_project_will_add_creator_as_project_admin
    coverage run --source='.' manage.py test project.tests.ProjectTest.test_project_create_invalid_project_type
  
  '''

  def test_project_delete_not_found_instance(self):
    response = self.client_1.delete(
      reverse('project:delete', kwargs={'pk':500})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def _test_project_delete(self):
    response = self.client_1.delete(
      reverse('project:delete', kwargs={'pk':3})
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def _test_project_delete_get_method(self):
    project_1 = Project.objects.get(pk=1)
    response = self.client_1.get(
      reverse('project:delete', kwargs={'pk':project_1.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'Test project 1')

  def _test_project_update_invalid(self):
    project_1 = Project.objects.get(pk=1)
    response = self.client_1.put(
      reverse('project:update', kwargs={'pk':project_1.id}),
      data=self.test_project_3,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_project_update(self):
    # project = Project.objects.get(pk=2)
    response = self.client_1.put(
      reverse('project:update', kwargs={'pk':2}),
      data=self.test_update,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(response.data['name'], 'Test project 1 updated')

  def test_project_update_get_method(self):
    # project = Project.objects.get(pk=1)
    response = self.client_1.get(
      reverse('project:update', kwargs={'pk':1})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'Test project 1')

  def test_create_project_will_add_creator_as_project_admin(self):
    response = self.client_1.post(
      reverse('project:create'),
      self.test_new_project_1,
      format='json'
    )
    project = Project.objects.get(pk=response.data['id'])
    collaborators = project.collaborators.all()
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(collaborators[0].name.username, self.test_user1.username)
    self.assertEqual(collaborators[0].position, 1)

  def test_project_create_existing_name_by_another_user(self):
    response = self.client_2.post(
      reverse('project:create'),
      self.test_project_2,
      format='json'
      )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_project_create_invalid_status(self):
    response = self.client_1.post(
      reverse('project:create'),
      self.test_project_invalid_status,
      format='json'
      )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_project_create_invalid_project_type(self):
    response = self.client_1.post(
      reverse('project:create'),
      self.test_project_invalid_project_type,
      format='json'
      )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_project_create_existing_name_by_user(self):
    response = self.client_1.post(
      reverse('project:create'),
      self.test_project_2,
      format='json'
      )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_project_create(self):
    response = self.client_1.post(
      reverse('project:create'),
      self.test_new_project_1,
      format='json'
      )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['name'], 'Test new project 1')

  def test_project_create_get_method(self):
    response = self.client_1.get(reverse('project:create'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], '')

  def test_get_project_details(self):
    # project_1 = Project.objects.get(pk=1)
    response = self.client.get(
      reverse('project:details', kwargs={'pk':2})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data["created_by"]["username"], self.test_user1.username)

  def test_get_project_list(self):
    response = self.client_1.get( reverse('project:list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 3)

