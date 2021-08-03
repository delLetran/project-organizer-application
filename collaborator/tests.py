# from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from project.models import Project
from collaborator.models import Collaborator
User = get_user_model()


class CollaboratorTest(APITestCase):
  def setUp(self):
    self.client_1 = APIClient()
    self.client_2 = APIClient()
    self.client_3 = APIClient()
    self.client_4 = APIClient()
    self.existing_project = {
      "name": "Existing Project",
      "description": "Project Existing ",
      "status": 1,
      "project_type": 3
    }
    self.existing_project_2 = {
      "name": "Existing Project 2",
      "description": "Project Existing 2 ",
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
      last_name='user2',
      password='@l03e1t1',
      is_staff=True,
      is_active=True
    )
    self.test_user3 = User.objects.create_user(
      email='test_user3@gmail.com',
      username='testuser3',
      first_name='test',
      last_name='user3',
      password='@l03e1t1',
      is_staff=True,
      is_active=True
    )
    self.test_user4 = User.objects.create_user(
      email='test_user4@gmail.com',
      username='testuser4',
      first_name='test',
      last_name='user4',
      password='@l03e1t1',
      is_staff=True,
      is_active=True
    )
    self.client_1.login(email=self.test_user1.email, password='@l03e1t1')
    self.client_2.login(email=self.test_user2.email, password='@l03e1t1')
    self.client_3.login(email=self.test_user3.email, password='@l03e1t1')
    self.client_4.login(email=self.test_user4.email, password='@l03e1t1')
    self.existing_project_res = self.client_1.post(
      reverse('project:create'),
      self.existing_project,
      format='json'
    )
    self.existing_project_2_res = self.client_2.post(
      reverse('project:create'),
      self.existing_project_2,
      format='json'
    )
    self.client_2.post(
      reverse('collaborator:invite', kwargs={'invitee':self.test_user3.username,'project_id':2})
    )
    self.client_2.post(
      reverse('collaborator:invite', kwargs={'invitee':self.test_user4.username,'project_id':2})
    )
    self.client_4.put(
      reverse('collaborator:accept', kwargs={'project_id':2})
    )


  '''
  coverage run --source='.' manage.py test collaborator.tests.CollaboratorTest.test_remove_creator
  '''
    
    

  def test_received_invites(self):
    response = self.client_2.get(reverse('collaborator:received-invites'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_sent_invites(self):
    response = self.client_2.get( reverse('collaborator:sent-invites'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 3)

  def test_leave_project(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user4.username)
    response = self.client_4.get(
      reverse('collaborator:leave', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    response = self.client_4.put(
      reverse('collaborator:leave', kwargs={'project_id':project_instance.id})
    )
    response = self.client_4.get(
      reverse('collaborator:leave', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_leave_project_get_method(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user4.username)
    response = self.client_4.get(
      reverse('collaborator:leave', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  '''
  coverage run --source='.' manage.py test collaborator.tests.CollaboratorTest.test_remove_creator
  '''
    
  def test_remove_creator_invalid(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user2.username)
    response = self.client_2.get(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    response = self.client_2.put(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    response = self.client_2.get(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_remove_collaborator(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user4.username)
    response = self.client_2.get(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    response = self.client_2.put(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    response = self.client_2.get(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_remove_collaborator_get_method(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user4.username)
    response = self.client_2.get(
      reverse('collaborator:remove', kwargs={'collaborator':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_cancel_invite(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user3.username)
    response = self.client_2.put(
      reverse('collaborator:cancel', kwargs={'invitee':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    response = self.client_2.get(
      # f'api/collaborator/{user}/{project_instance.id}/cancel/'
      reverse('collaborator:cancel', kwargs={'invitee':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_cancel_invite_get_method(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user3.username)
    response = self.client_2.get(
      reverse('collaborator:cancel', kwargs={'invitee':user, 'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_decline_invite(self):
    project_instance = Project.objects.get(pk=2) 
    user = User.objects.get(username=self.test_user3.username)
    response = self.client_3.put(
      reverse('collaborator:decline', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    response = self.client_3.get(
      reverse('collaborator:decline', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_decline_invite_get_method(self):
    project_instance = Project.objects.get(pk=2) 
    response = self.client_3.get(
      reverse('collaborator:decline', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_accept_uninvited_collaborator(self):
    project_instance = Project.objects.get(pk=1)
    user = User.objects.get(username=self.test_user3.username)
    response = self.client_3.put(
      reverse('collaborator:accept', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_accept_invite(self):
    project_instance = Project.objects.get(pk=2)
    user = User.objects.get(username=self.test_user3.username)
    response = self.client_3.put(
      reverse('collaborator:accept', kwargs={'project_id':project_instance.id})
    )
    collaborator = Collaborator.objects.get(project=project_instance.id, name=user)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(collaborator.name.username, user.username)
    self.assertEqual(collaborator.status, 'Joined')

  def test_accept_invite_get_method(self):
    project_instance = Project.objects.get(pk=2) 
    response = self.client_3.get(
      reverse('collaborator:accept', kwargs={'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_invite_already_invited_collaborator(self):
    project_instance = Project.objects.get(pk=2)
    user = User.objects.get(username=self.test_user3.username)
    response = self.client_2.post(
      reverse('collaborator:invite', kwargs={'invitee':user,'project_id':project_instance.id})
    )
    collaborator = Collaborator.objects.get(project=project_instance.id, name=user)
    instance_count = len(Collaborator.objects.all().filter(project=project_instance.id, name=user))
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(instance_count, 1)

  def test_invite_collaborator(self): 
    project_instance = Project.objects.get(pk=1)
    user = User.objects.get(username=self.test_user2.username)
    response = self.client_1.post(
      reverse('collaborator:invite', kwargs={'invitee':user,'project_id':project_instance.id})
    )
    collaborator = Collaborator.objects.get(project=project_instance.id, name=user)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(collaborator.status, 'Invited')


  def test_invite_collaborator_get_method(self):
    project_instance = Project.objects.get(pk=1)
    user = User.objects.get(username=self.test_user2.username)
    response = self.client_1.get(
      reverse('collaborator:invite', kwargs={'invitee':user,'project_id':project_instance.id})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def _test_list_collaborator(self): 
    project_instance = Project.objects.get(pk=1)
    
    response = self.client_1.get(reverse('collaborator:list', kwargs={'project_id':project_instance.id}))
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)





