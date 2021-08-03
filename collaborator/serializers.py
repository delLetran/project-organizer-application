from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.validators import ValidationError

from .models import Collaborator
from project.models import Project
User = get_user_model()


# SentInviteSerializer
# ReceivedInviteSerializer

class CreatedBySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']


# class ProjectSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Project
#     fields = ['id', 'name', 'slug', 'description', 'project_type', 'status', 'created_by', 'collaborators']


class CollaboratorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collaborator
    fields = ["name", "project", "position", "status"]

class CollaboratorUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collaborator
    fields = ["name", "project", "position"]

class CollaboratorCreateSerializer(serializers.ModelSerializer):
  # project = ProjectSerializer(write_only=True)

  class Meta:
    model = Collaborator
    fields = ["name", "project", "position", "inviter"]
    # validators = [
    #   UniqueTogetherValidator(
    #     queryset=Project.objects.all(),
    #     fields=('name', 'project'),
    #     message=_("This user has already been invited, waiting for user to join the group.")
    #   )
    # ]


  def validate(self, data):
    user = data['name']
    project = data['project']
    has_received_an_invite = Collaborator.objects.all().filter(
      name=user,
      project=project.id
    ).exists()
    if has_received_an_invite:
      raise serializers.ValidationError(f"{user} has already been invited, waiting for user to join the group.")
    return data
        