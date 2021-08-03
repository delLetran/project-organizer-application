from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.utils.text import slugify

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from .models import  Task
from activity.models import Activity

User = get_user_model()


class CreatedBySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']

class ActivitySerializer(serializers.ModelSerializer):  
  class Meta:
    model = Activity
    fields = ["name", "status", "created_by"]

# class ActivitySerializer(serializers.ModelSerializer):
#   tasks = TaskSerializer(read_only=True)

#   class Meta:
#     model = Activity
#     fields = ["name", "status", "tasks", "project", "created_by"]


class TaskSerializer(serializers.ModelSerializer):
  activity = ActivitySerializer(read_only=True)
  class Meta:
    model = Task
    fields = ["name", "desciption", "importance", "due_date", "activity", "created_by"]


class TaskUpdateSerializer(serializers.ModelSerializer):
  activity = ActivitySerializer(read_only=True)
  class Meta:
    model = Task
    fields = ["name", "desciption", "importance", "due_date", "activity", "created_by"]

class TaskCreateSerializer(serializers.ModelSerializer):
  # activity = TaskSerializer(read_only=True)
  class Meta:
    model = Task
    fields = ["name", "desciption", "importance", "due_date", "activity", "created_by"]
    validators = [
      UniqueTogetherValidator(
        queryset=Task.objects.all(),
        fields=('name', 'activity'),
        message=_("Task name has already been used under this activity.")
      )
    ]

