from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from django.utils.text import slugify

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()
from project.models import Project
from collaborator.models import Collaborator
from .models import Associate


# class ChoicesSerializer(serializers.ChoiceField):
#   def to_representation(self, value):
#     if value in self.choices.keys():
#       return self.choices[value]

#     self.fail("invalid_choice", input=value)
#     return None

#   def to_internal_value(self, data):
#     for key, value in self.choices.items():
#       if value == data:
#         return key
#     self.fail("invalid_choice", input=data)
#     return None



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'first_name', 'last_name', 'job_title']

class AssociateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Associate
    fields = [ 'id', 'sender', 'receiver', 'status']

class ReceivedInviteSerializer(serializers.ModelSerializer):
  sender = UserSerializer(read_only=True)
  class Meta:
    model = Associate
    fields = [ 'id', 'sender', 'status']

class SentInviteSerializer(serializers.ModelSerializer):
  receiver = UserSerializer(read_only=True)
  class Meta:
    model = Associate
    fields = [ 'id', 'receiver', 'status']

class PeerUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Associate
    fields = ['sender']

class PeerCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Associate
    fields = [ 'id', 'sender', 'receiver']
    validators = [
      UniqueTogetherValidator(
        queryset=Associate.objects.all(),
        fields=('sender', 'receiver'),
        message=_("Invite has already been sent to this user.")
      )
    ]

  def validate(self, data):
    user = data['sender']
    has_received_an_invite  = Associate.objects.all().filter(
      sender=data['receiver'], 
      receiver=user
    ).exists()
    if has_received_an_invite :
      raise serializers.ValidationError(f"{user} already sent you an invite.")
    return data

