from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import json

from .models import Associate
User = get_user_model()

#Test Views

    # from django.test import TestCase, Client

class AssociateTest(APITestCase):
  def setUp(self):
    self.client_inviter = APIClient()
    self.client_invitee = APIClient()
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
      is_active=True
    )
    self.client_inviter.login(email=self.test_user1.email, password='@l03e1t1')
    self.client_invitee.login(email=self.test_user2.email, password='@l03e1t1')
  
    self.receiver = {"receiver": "testuser2"}
    self.sender   = {"receiver": "testuser1"}

  def test_add_inviter_to_associate_invalid(self):
    response = self.client_inviter.post(
      reverse('associate-invite'),
      self.receiver,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    response = self.client_invitee.post(
      reverse('associate-invite'),
      self.sender,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_accept_associate(self):
    response = self.client_inviter.post(
      reverse('associate-invite'),
      self.receiver,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    response = self.client_invitee.put(reverse('associate-accept', kwargs={"username":"testuser1"}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_add_associate(self):
    response = self.client_inviter.post(
      reverse('associate-invite'),
      self.receiver,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
  def test_invite_get_method(self): 
    response = self.client_inviter.get(reverse('associate-invite'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)












class GetMutualAssociateTest(APITestCase):
  def setUp(self): 
    self.client = APIClient()
    self.test_user1 = User.objects.create_user(
      email='test_user1@gmail.com',
      username='testuser1',
      first_name='test',
      last_name='user1',
      password='@l03e1t1',
      is_staff=True,
      is_active=True
    )

  def test_get_mutual_associates(self):
    user = User.objects.get(pk=1)
    self.assertEqual(user.username, 'testuser1')
    # data = user.get_associate_with_mutual_associates_list()
    # print(data)
