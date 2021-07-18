from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth import authenticate
from .serializers import UserSerializer, OwnerSerializer
from .forms import SignUpForm
from .tokens import create_token, get_user_token
import json

User = get_user_model()
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
#Test Views

class DeleteUserTest(APITestCase):
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
    self.test_user2 = User.objects.create_user(
      email='test_user2@gmail.com',
      username='testuser2',
      first_name='test',
      last_name='user2',
      password='@l03e1t2',
      is_staff=False,
      is_active=True
    )
    self.test_user3 = User.objects.create_user(
      email='test_user3@gmail.com',
      username='testuser3',
      first_name='test',
      last_name='user3',
      password='@l03e1t3',
      is_staff=False,
      is_active=True
    )
    self.test_user4 = User.objects.create_user(
      email='test_user4@gmail.com',
      username='testuser4',
      first_name='test',
      last_name='user4',
      password='@l03e1t4',
      is_staff=False,
      is_active=True
    )

  def test_delete_owner_account(self):
    self.client.login(email=self.test_user1.email, password='@l03e1t1')
    response = self.client.delete(reverse('user-delete'))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_get_method(self):
    self.client.login(email=self.test_user1.email, password='@l03e1t1')
    response = self.client.get( reverse('user-delete'))
    profile = User.objects.get(username=self.test_user1.username)
    serializer = OwnerSerializer(profile)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    

class UpdateUserTest(TestCase):

  def setUp(self): 
    self.client = APIClient()
    self.update_email = {
      "email":"updated_email@gmail.com",
      "username":"testuser1"
    }
    self.update_username = {
      "username":"updated_username",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1"
    }
    self.update_fullname = {
      "username":"testuser1",
      "first_name":"updated",
      "last_name":"updated",  
    }
    self.update_password = {
      "old_password":"@l03e1t1",
      "new_password1":"@l03e1t1_new",
      "new_password2":"@l03e1t1_new",
    }
    self.update_not_match_password = {
      "old_password":"@l03e1t1",
      "new_password1":"@l03e1t1_not",
      "new_password2":"@l03e1t1_match",
    }
    self.update_password_incorrect_old_password = {
      "old_password":"@l03e1t1_incorrect",
      "new_password1":"@l03e1t1_new",
      "new_password2":"@l03e1t1_new",
    }
    self.update_invalid_password = {
      "old_password":"@l03e1t1",
      "new_password1":"@l03e1t1_new",
      "new_password2":"@l03e1t1_new123",
    }
    self.invalid_update = {
      "username":"existing_username",
      "first_name":"updated",
      "last_name":"updated"
    }

    self.test_user1 = User.objects.create_user(
      email='test_user1@gmail.com',
      username='testuser1',
      first_name='test',
      last_name='user',
      password='@l03e1t1',
      is_active=True
    )

    self.existing_user = User.objects.create_user(
      email='existing_email@gmail.com',
      username='existing_username',
      first_name='existing',
      last_name='user',
      password='@l03e1t3'
    )
    self.client.login(email=self.test_user1.email, password='@l03e1t1')

  def test_update_password(self):
    response = self.client.put(
      reverse('user-update-password'),
      self.update_password,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_update_password_not_match(self):
    response = self.client.put(
      reverse('user-update-password'),
      self.update_not_match_password,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_update_password_incorrect_old_password(self):
    response = self.client.put(
      reverse('user-update-password'),
      self.update_password_incorrect_old_password,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_password_update_get_method(self):
    response = self.client.get(reverse('user-update-password'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_update_email(self):
    response = self.client.put(
      reverse('user-update'),
      self.update_email,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_update_username(self):
    response = self.client.put(
      reverse('user-update'),
      self.update_username,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_update_fullname(self):
    response = self.client.put(
      reverse('user-update'),
      self.update_fullname,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_user_update_get_method(self):
    response = self.client.get(reverse('user-update'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  def test_invalid_updates(self):
    response = self.client.put(
      reverse('user-update'),
      self.invalid_update,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


  # def test_update_email(self):
  #   response = self.client.put(
  #     reverse('user-update', kwargs={'username':self.test_user1.username}),
  #     self.update_email,
  #     format='json'
  #   )
  #   self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ActivateUserAccountTest(TestCase):

  def setUp(self): 
    self.client = APIClient()
    self.test_user2 = {
      "email":"test_user2@gmail.com",
      "username":"testuser2",
      "first_name":"test",
      "last_name":"valid_user",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1",
      "is_active":False
    }
    
    self.test_user1 = User.objects.create_user(
      email='test_user1@gmail.com',
      username='testuser1',
      first_name='test',
      last_name='user',
      password='@l03e1t1',
      is_active=True
    )

    self.client.login(email=self.test_user1.email, password='@l03e1t1')

  def test_resend_account_verification(self):
    response = self.client.post(
      reverse('user-signup'),
      self.test_user2,
      format = 'json'
    )
    form = SignUpForm(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    response = self.client.get(reverse('user-resend-verification'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_account_activation(self):
    response = self.client.post(
      reverse('user-signup'),
      self.test_user2,
      format = 'json'
    )
    form = SignUpForm(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(form.data, response.data)

    uid = urlsafe_base64_encode(force_bytes(2))
    token = get_user_token(2)
    response = self.client.get(
      reverse('user-activate', kwargs={
        'uid': uid,
        'token': token
        })
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    response = self.client.get(
      reverse('user-activate', kwargs={
        'uid': uid,
        'token': 'unknowntokenorapntoanidioa;'
        })
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class GetDetailUserTest(APITestCase):
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
    self.test_user2 = User.objects.create_user(
      email='test_user2@gmail.com',
      username='testuser2',
      first_name='test',
      last_name='user2',
      password='@l03e1t2',
      is_staff=False,
      is_active=True
    )
    self.test_user3 = User.objects.create_user(
      email='test_user3@gmail.com',
      username='testuser3',
      first_name='test',
      last_name='user3',
      password='@l03e1t3',
      is_staff=False,
      is_active=True
    )
    self.test_user4 = User.objects.create_user(
      email='test_user4@gmail.com',
      username='testuser4',
      first_name='test',
      last_name='user4',
      password='@l03e1t4',
      is_staff=False,
      is_active=True
    )
    
    self.client.login(email=self.test_user1.email, password='@l03e1t1')

  def test_get_invalid_user(self):
    response = self.client.get( reverse('user-details', kwargs={'username':'unknown_user'}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_get_valid_user(self):
    response = self.client.get( reverse('user-details', kwargs={'username':self.test_user1.username}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_owner_data(self):
    response = self.client.get( reverse('user-details', kwargs={'username':self.test_user1.username}))
    profile = User.objects.get(email=self.test_user1.email)
    serializer = OwnerSerializer(profile)
    self.assertEqual(response.data, serializer.data)

  def test_get_other_profile_data(self):
    response = self.client.get( reverse('user-details', kwargs={'username':self.test_user2.username}))
    profile = User.objects.get(pk=2)
    serializer = UserSerializer(profile)
    self.assertEqual(response.data, serializer.data)


class CreateUserTest(TestCase):

  def setUp(self): 
    self.client = APIClient()
    self.valid_user = {
      "email":"test_user1@gmail.com",
      "username":"testuser1",
      "first_name":"test",
      "last_name":"valid_user",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1",
      "is_active":True
    }
    self.invalid_username = {
      "email":"test_invalid_username@gmail.com",
      "username":"",
      "first_name":"test",
      "last_name":"invalid_username",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1",
      "is_active":True
    }
    self.invalid_email = {
      "email":"test_superuser1@gmail",
      "username":"testuser1",
      "first_name":"test",
      "last_name":"invalid_email",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1",
      "is_active":True
    }
    self.existing_username = {
      "email":"test_existing_username@gmail.com",
      "username":"existing_username",
      "first_name":"test",
      "last_name":"existing_username",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1",
      "is_active":True
    }
    self.existing_email = {
      "email":"existing_email@gmail.com",
      "username":"existing_email",
      "first_name":"test",
      "last_name":"existing_email",
      "password1":"@l03e1t1",
      "password2":"@l03e1t1",
      "is_active":True
    }
    self.invalid_password = {
      "email":"test_invalid_password@gmail.com",
      "username":"invalid_password",
      "first_name":"test",
      "last_name":"invalid_password",
      "password1":"@l03e1t1",
      "password2":"@l03e1t13",
      "is_active":True
    }

    self.existing_user = User.objects.create_user(
      email='existing_email@gmail.com',
      username='existing_username',
      first_name='existing',
      last_name='user',
      password='@l03e1t3',
      is_active=True
    )

  def test_get_signup_form(self):
    response = self.client.get(reverse('user-signup'))
    form = SignUpForm(response.data)
    self.assertEqual(form.data, response.data)

  def test_create_valid_user(self):
    response = self.client.post(
      reverse('user-signup'),
      self.valid_user,
      format = 'json'
    )
    form = SignUpForm(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(form.data, response.data)

  def test_create_existing_username(self):
    response = self.client.post(
      reverse('user-signup'),
      self.existing_username,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_existing_email(self):
    response = self.client.post(
      reverse('user-signup'),
      self.existing_email,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_invalid_username(self):
    response = self.client.post(
      reverse('user-signup'),
      self.invalid_username,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_create_invalid_password(self):
    response = self.client.post(
      reverse('user-signup'),
      self.invalid_password,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#Test Models

class UserManagerTest(TestCase):
  def setUp(self):
    self.superuser = User.objects.create_superuser(
      email='superuser@gmail.com',
      username='superuser',
      first_name='super',
      last_name='user',
      password='@l03e1t3'
    )
    self.testuser = User.objects.create_user(
      email='testuser@gmail.com',
      username='testuser',
      first_name='test',
      last_name='user',
      password='@l03e1t3'
    )
  def test_create_user(self):
    self.assertFalse(self.testuser.is_staff)
    self.assertFalse(self.testuser.is_superuser)
    self.assertFalse(self.testuser.is_active)

  def test_create_invalid_user_email(self):
    with self.assertRaisesMessage(ValueError, 'Enter a valid email address'):
      User.objects.create_user(
        email='',
        username='invalid_user',
        first_name='invalid',
        last_name='user',
        password='@l03e1t3'
      )

  def test_create_super_user(self):
    self.assertTrue(self.superuser.is_staff)
    self.assertTrue(self.superuser.is_superuser)
    self.assertTrue(self.superuser.is_active)

  def test_create_false_is_staff_super_user(self):
    with self.assertRaisesMessage(ValueError, 'is_staff must be set True for superuser'):
      User.objects.create_superuser(
        email='superuser@gmail.com',
        username='superuser',
        first_name='super',
        last_name='user',
        password='@l03e1t3',
        is_staff=False
      )

  def test_create_false_is_superuser_super_user(self):
    with self.assertRaisesMessage(ValueError, 'is_superuser must be set True for superuser'):
      User.objects.create_superuser(
        email='superuser@gmail.com',
        username='superuser',
        first_name='super',
        last_name='user',
        password='@l03e1t3',
        is_superuser=False
      )
