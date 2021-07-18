from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.utils.text import slugify

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from .models import Activity
from project.models import Project
# from task.models import Task
User = get_user_model()


class CreatedBySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = [ 'id', 'username', 'first_name', 'last_name', 'job_title']


# class TaskSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Task
#     fields = [ 'id', 'username', 'first_name', 'last_name', 'job_title']


# class ActivitySerializer(serializers.ModelSerializer):
#   task = TaskSerializer(read_only=True)

#   class Meta:
#     model = Activity
#     fields = ["name", "status", "task", "project", "created_by"]


class NoteCreateSerializer(serializers.ModelSerializer):
#   project = ProjectSerializer(read_only=True)

  class Meta:
    model = Note
    fields = ["tag", "description", "project", "created_by"]
    # validators = [
    #   UniqueTogetherValidator(
    #     queryset=Project.objects.all(),
    #     fields=('name', 'created_by'),
    #     message=_("User has already created a project with this name.")
    #   )
    # ]

