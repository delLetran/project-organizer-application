from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework.exceptions import ValidationError
import json

from .models import Associate
from .serializers import PeerCreateSerializer
User = get_user_model()

#Test Views

    # from django.test import TestCase, Client

class AssociateTest(APITestCase):
  def setUp(self):
    self.client_inviter = APIClient()
    self.client_invitee = APIClient()
    self.client_1 = APIClient()
    self.client_2 = APIClient()
    self.client_3 = APIClient()
    self.client_4 = APIClient()
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
    self.test_client1 = User.objects.create_user(
      email='test_client1@gmail.com',
      username='testclient1',
      first_name='test',
      last_name='client1',
      password='@l03e1t1',
      is_active=True
    )
    self.test_client2 = User.objects.create_user(
      email='test_client2@gmail.com',
      username='testclient2',
      first_name='test',
      last_name='client2',
      password='@l03e1t1',
      is_active=True
    )
    self.test_client3 = User.objects.create_user(
      email='test_client3@gmail.com',
      username='testclient3',
      first_name='test',
      last_name='client3',
      password='@l03e1t1',
      is_active=True
    )
    self.test_client4 = User.objects.create_user(
      email='test_client4@gmail.com',
      username='testclient4',
      first_name='test',
      last_name='client3',
      password='@l03e1t1',
      is_active=True
    )
    self.client_inviter.login(email=self.test_user1.email, password='@l03e1t1')
    self.client_invitee.login(email=self.test_user2.email, password='@l03e1t1')
    self.client_1.login(email=self.test_client1.email, password='@l03e1t1')
    self.client_2.login(email=self.test_client2.email, password='@l03e1t1')
    self.client_3.login(email=self.test_client3.email, password='@l03e1t1')
    self.client_4.login(email=self.test_client4.email, password='@l03e1t1')
    self.client_1_invite_resp = self.client_1.post( reverse('associate:invite',
      kwargs={'invitee':f'{self.test_client2.username}'}), {}, format='json'
    )
    self.client_1_invite_resp2 = self.client_1.post( reverse('associate:invite', 
      kwargs={'invitee':f'{self.test_client3.username}'}), {}, format='json'
    )
    self.client_3_accept_resp = self.client_3.put( reverse('associate:accept', 
      kwargs={'inviter':f'{self.test_client1.username}'}),{}, format='json'
    )
    self.client_4_invite_resp = self.client_4.post( reverse('associate:invite',
      kwargs={'invitee':f'{self.test_client1.username}'}), {}, format='json'
    )
    self.client_4_invite_resp = self.client_4.post( reverse('associate:invite',
      kwargs={'invitee':f'{self.test_client3.username}'}), {}, format='json'
    )
    self.client_3_accept_resp = self.client_3.put( reverse('associate:accept', 
      kwargs={'inviter':f'{self.test_client4.username}'}),{}, format='json'
    )

  # associate mutual list test

  def test_associate_user_mutual_list(self):
    response = self.client_1.get(
      reverse('associate:user-mutual-list', kwargs={'username':f'{self.test_client4.username}'})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # associate mutual list test

  def test_associate_mutual_list(self):
    response = self.client_1.get(reverse('associate:mutual-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # associate list test

  def test_associate_list(self):
    response = self.client_1.get( reverse('associate:list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # received-invites test

  def test_received_invites(self):
    response = self.client_1.get( reverse('associate:received-invites'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # sent-invites test

  def test_sent_invites(self):
    response = self.client_1.get( reverse('associate:sent-invites'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  # cancel test 
  
  def test_cancel_invite_not_in_waiting_list(self):
    response = self.client_1.put(
      reverse('associate:cancel', kwargs={'invitee':f'{self.test_client3.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    self.assertEqual(response.data['error'], 'User not in waiting list')
    
  def test_cancel_invite_not_found_instance(self):
    response = self.client_2.put(
      reverse('associate:cancel', kwargs={'invitee':'no_user'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
  
  def test_cancel_invite(self):
    response = self.client_1.put(
      reverse('associate:cancel', kwargs={'invitee':f'{self.test_client2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_cancel_invite_get_method_not_found_instance(self):
    response = self.client_2.get(
      reverse('associate:cancel', kwargs={'invitee':'no_user'})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_cancel_invite_get_method(self): 
    response = self.client_1.get(
      reverse('associate:cancel',kwargs={'invitee':f'{self.test_client2.username}'})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # dissociate test 

  def test_dissociate_not_accepted_associate(self):
    response = self.client_2.put(
      reverse('associate:dissociate', kwargs={'associate':f'{self.test_client1.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
  
  def test_dissociate_associate_not_found_instance(self):
    response = self.client_2.put(
      reverse('associate:dissociate', kwargs={'associate':'no_user'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    self.assertEqual(response.data['error'], 'User not in associate list')

  def test_dissociate_associate(self):
    response = self.client_3.put(
      reverse('associate:dissociate', kwargs={'associate':f'{self.test_client1.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_dissociate_associate_get_method_not_found_instance(self):
    response = self.client_2.get(
      reverse('associate:dissociate', kwargs={'associate':'no_user'})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_dissociate_associate_get_method(self): 
    response = self.client_1.get(
      reverse('associate:dissociate',kwargs={'associate':f'{self.test_client3.username}'})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  # decline test 

  def test_decline_invite_not_found_instance(self):
    response = self.client_2.put(
      reverse('associate:decline', kwargs={'inviter':'no_user'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_decline_invite(self):
    response = self.client_2.put(
      reverse('associate:decline', kwargs={'inviter':f'{self.test_client1.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_decline_invite_get_method_not_found_instance(self):
    response = self.client_2.get(
      reverse('associate:decline', kwargs={'inviter':'no_user'})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_decline_invite_get_method(self): 
    response = self.client_2.get(
      reverse('associate:decline',kwargs={'inviter':f'{self.test_client1.username}'})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # accept test 
    
  def test_accept_associate_not_found_instance(self):
    response = self.client_2.put(
      reverse('associate:accept', kwargs={'inviter':'no_user'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
  def test_accept_associate_invite(self):
    response = self.client_2.put(
      reverse('associate:accept', kwargs={'inviter':f'{self.test_client1.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_accept_invite_get_method_not_found_instance(self):
    response = self.client_2.get(
      reverse('associate:accept', kwargs={'inviter':'no_user'})
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
  
  def test_accept_invite_get_method(self): 
    response = self.client_2.get(
      reverse('associate:accept', kwargs={'inviter':f'{self.test_client1.username}'})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  # invite test 

  def test_associate_invite_inviter_invalid(self):
    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    response = self.client_invitee.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user1.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_associate_invite_not_found_user(self):
    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':'no_user'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
  def test_associate_invite_already_received(self):
    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    with self.assertRaisesMessage(ValidationError, 'User already sent you an invite.'):
      data = {
        'sender': self.test_user2.pk,
        'receiver': self.test_user1.pk
      }
      serializer = PeerCreateSerializer(data=data) 
      serializer.is_valid(raise_exception=True)

  def test_associate_invite_already_sent(self):
    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    # with self.assertRaisesMessage(ValidationError, 'Invite has already been sent to this user.'):
    #   data = {
    #     'sender': self.test_user1.pk,
    #     'receiver': self.test_user2.pk
    #   }
    #   serializer = PeerCreateSerializer(data=data) 
    #   serializer.is_valid(raise_exception=True)
    
  def test_associate_invite(self):
    response = self.client_inviter.post(
      reverse('associate:invite', kwargs={'invitee':f'{self.test_user2.username}'}),
      {}, format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
  def test_invite_get_method(self): 
    response = self.client_inviter.get(
      reverse('associate:invite',kwargs={'invitee':f'{self.test_user2.username}'})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
