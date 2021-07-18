from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

from django.contrib.auth import get_user_model
User = get_user_model()

#Test Views



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