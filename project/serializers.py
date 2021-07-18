from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.utils.text import slugify

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from .models import Project
from collaborator.models import Collaborator
from activity.models import Activity
from task.models import Task
User = get_user_model()


class ChoicesSerializer(serializers.ChoiceField):
  def to_representation(self, value):
    if value in self.choices.keys():
      return self.choices[value]

    self.fail("invalid_choice", input=value)
    return None

  def to_internal_value(self, data):
    for key, value in self.choices.items():
      if value == data:
        return key
    self.fail("invalid_choice", input=data)
    return None


class CreatedBySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']


class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = [ 'id', 'name', 'desciption']


class ActivitySerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(read_only=True, many=True)
  # project = ProjectSerializer(read_only=True)

  class Meta:
    model = Activity
    fields = ["name", "status", "tasks", "created_by"]


class CollaboratorSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']


class ProjectSerializer(serializers.ModelSerializer):
  created_by = CreatedBySerializer(read_only=True)
  status = ChoicesSerializer(choices=Project.STATUS.choices)
  project_type = ChoicesSerializer(choices=Project.TYPE.choices)
  collaborators = CollaboratorSerializer(read_only=True, many=True)
  activities = ActivitySerializer(read_only=True, many=True)
  # schedule = ScheduleSerializer(read_only=True)

  class Meta:
    model = Project
    fields = "__all__"
    fields = ['id', 'name', 'slug', 'description', 'project_type', 'status', 'activities', 'created_by', 'collaborators']
  

class ProjectUpdateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ["name", "slug", "description", "status", "project_type", "created_by"]
    read_only_fields = ['created_by']
    
  # def validate(self, data):
  # if data['start_date'] > data['end_date']:
  #   raise serializers.ValidationError({"end_date": "finish must occur after start"})
  # return data


class ProjectCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ["name", "description", "status", "project_type", "created_by"]
    # write_only_fields=['created_by']
    validators = [
      UniqueTogetherValidator(
        queryset=Project.objects.all(),
        fields=('name', 'created_by'),
        message=_("User has already created a project with this name.")
      )
    ]


# class CollaboratorSerializer(serializers.ModelSerializer):
#   collaborator = CollaboratorSerializer(read_only=True) 

#   class Meta:
#     model = Collaborator
#     fields = "__all__" 
