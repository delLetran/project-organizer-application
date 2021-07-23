# from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from .models import Project

User = get_user_model()
from collaborator.models import Collaborator


class ProjectUpdateTest(APITestCase):
  def setUp(self):
    self.client = APIClient()
    self.another_client = APIClient()
    self.invalid_project = {
      "name":"invalid_project"
    }
    self.test_project1 = {
        "name": "Test project 1",
        "description": "Project testing ",
        "status": 1,
        "project_type": 3
    }
    self.test_project2 = {
        "name": "Test project 2",
        "description": "Project testing ",
        "status": 2,
        "project_type": 2
    }
    self.test_project3 = {
        "name": "Test project3",
        "description": "Project changed_created_by ",
        "created_by": 3,
        "status": 1,
        "project_type": 3
    }
    self.test_project4 = {
        "name": "Test project 4 ",
        "description": "Project changed_created_by ",
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
    self.client.login(email=self.test_user1.email, password='@l03e1t1')
    self.project_1 = self.client.post(
      reverse('project-create'),
      self.test_project1,
      format='json'
    )
    self.project_2 = self.client.post(
      reverse('project-create'),
      self.test_project2,
      format='json'
    )
    self.project_3 = self.client.post(
      reverse('project-create'),
      self.test_project3,
      format='json'
    )
    self.another_client.login(email=self.test_user2.email, password='@l03e1t1')
    self.project_4 = self.another_client.post(
      reverse('project-create'),
      self.test_project4,
      format='json'
    )

class ProjectGetTest(APITestCase):
  def setUp(self):
    self.client = APIClient()
    self.another_client = APIClient()
    self.invalid_project = {
      "name":"invalid_project"
    }
    self.test_project1 = {
        "name": "Test project 1",
        "description": "Project testing ",
        "status": 1,
        "project_type": 3
    }
    self.test_project2 = {
        "name": "Test project 2",
        "description": "Project testing ",
        "status": 2,
        "project_type": 2
    }
    self.test_project3 = {
        "name": "Test project3",
        "description": "Project changed_created_by ",
        "created_by": 3,
        "status": 1,
        "project_type": 3
    }
    self.test_project4 = {
        "name": "Test project 4 ",
        "description": "Project changed_created_by ",
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
    self.client.login(email=self.test_user1.email, password='@l03e1t1')
    self.project_1 = self.client.post(
      reverse('project-create'),
      self.test_project1,
      format='json'
    )
    self.project_2 = self.client.post(
      reverse('project-create'),
      self.test_project2,
      format='json'
    )
    self.project_3 = self.client.post(
      reverse('project-create'),
      self.test_project3,
      format='json'
    )
    self.another_client.login(email=self.test_user2.email, password='@l03e1t1')
    self.project_4 = self.another_client.post(
      reverse('project-create'),
      self.test_project4,
      format='json'
    )
  def test_get_project_list(self):
    response = self.client.get( reverse('project-list'))
    self.assertEqual(len(response.data), 3)


class ProjectTest(APITestCase):
  def setUp(self):
    self.client = APIClient()
    self.invalid_project = {
      "name":"invalid_project"
    }
    self.existing_project = {
        "name": "Existing Project",
        "description": "Project Existing ",
        # "slug":"existing-project-slug-1",
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
    self.test_user3 = User.objects.create_user(
      email='test_user3@gmail.com',
      username='testuser3',
      first_name='test',
      last_name='user1',
      password='@l03e1t1',
      is_active=True
    )
    self.client.login(email=self.test_user1.email, password='@l03e1t1')
    self.existing_project_response = self.client.post(
      reverse('project-create'),
      self.existing_project,
      format='json'
    )
    # print(self.existing_project_response.data)
    self.test_project2 = {
        "name": "Test project 1",
        "description": "Project testing ",
        "status": 1,
        "project_type": 3
    }
    self.test_project3 = {
        "name": "Test project3",
        "description": "Project changed_created_by ",
        "created_by": 3,
        "status": 1,
        "project_type": 3
    }

    self.existing_project_by_user = {
        "name": "Existing Project",
        "description": "Project testing ",
        "status": 1,
        "project_type": 3
    }

  def test_get_project_details(self):
    project_1 = Project.objects.get(pk=1)
    existing_project_slug = project_1.slug
    response = self.client.get(
      reverse('project-details', kwargs={'slug':existing_project_slug})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data["created_by"]["username"], self.test_user1.username)

  def test_create_project(self): 
    response = self.client.post(
      reverse('project-create'),
      self.test_project2,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def _test_create_project_will_add_creator_as_project_admin(self):
    collaborator = Collaborator.objects.get(pk=1)
    response = self.client.post(
      reverse('project-create'),
      self.test_project2,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(collaborator.collaborator.username, self.test_user1.username)
    self.assertEqual(collaborator.position, 1)

  def test_create_existing_project_by_user(self):
    response = self.client.post(
      reverse('project-create'),
      self.existing_project_by_user,
      format='json'
      )
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


  # def test_add_collaborator(self):
  #   self.test_project.add_collaborator(test_user2)