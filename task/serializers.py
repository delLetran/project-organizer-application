from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.utils.text import slugify

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from .models import Activity, Task

User = get_user_model()


class CreatedBySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']


class ActivitySerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(read_only=True)

  class Meta:
    model = Activity
    fields = ["name", "status", "tasks", "project", "created_by"]


class TaskCreateSerializer(serializers.ModelSerializer):
  # activity = TaskSerializer(read_only=True)
  class Meta:
    model = Activity
    fields = ["name", "status", "activity", "created_by"]
    # validators = [
    #   UniqueTogetherValidator(
    #     queryset=Project.objects.all(),
    #     fields=('name', 'created_by'),
    #     message=_("User has already created a project with this name.")
    #   )
    # ]

