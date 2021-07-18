from django.shortcuts import get_object_or_404

from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


def create_token(user):
  try:
    delete_user_token(user)
  except:
    pass
  token = Token.objects.create(user=user)
  return token.key

def get_user_token(user):
  token = get_object_or_404(Token, user=user)
  return token.key
  
def delete_user_token(user):
  token = get_object_or_404(Token, user=user)
  token.delete()
  
def is_user_token_expired(user):
  # token = get_object_or_404(Token, user=user)
  token = Token.objects.get(user=user)
  now = timezone.now()
  created = token.created
  diff = (now-created).seconds
  if diff >= 86400:
    token.delete()
    return True
  else:
    return False


# from django.contrib.auth.tokens import PasswordResetTokenGenerator  
# from django.utils import six

# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):  
#         def _make_hash_value(self, user, timestamp):  
#             return (  
#                 six.text_type(user.pk) + six.text_type(timestamp) +  
#                 six.text_type(user.is_active)  
#             )
# account_activation_token = AccountActivationTokenGenerator()
