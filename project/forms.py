from django import forms
from django.contrib.auth import get_user_model

from rest_framework import status 
from .models import Project

User = get_user_model()


class ProjectForm(forms.ModelForm):
  
  class Meta:
    model = Project
    fields = ("name", "slug", "description", "status", "project_type", "created_by")
    # read_only_fields = ('created_by')

  def save(self, request, *args, **kwargs):
    self.instance.created_by = request.user
    return super().save(*args, **kwargs)





class ProjectUpdateForm(forms.ModelForm):
  
  class Meta:
    model = Project
    fields = ("name", "slug", "description", "status", "project_type", "created_by")
    read_only_fields = ('created_by')













  
  
# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model

# from rest_framework import status 
# from .models import Project

# User = get_user_model()


  # def save(self, request, *args, **kwargs):
  #   self.instance.created_by = request.user
  #   return super(Project, self).save(*args, **kwargs)
    # return super().save(*args, **kwargs)

  # def clean_name(self):
  #   _name = self.cleaned_data["name"]
  #   name = _name.lower()

  #   if name == 'invalid_project' :
  #     raise ValidationError(
  #       _(f"Project name '{_name}' is invalid."),
  #       code='invalid'
  #     )
  #   # if Project.objects.filter(name=name).exists() :
  #   #   raise ValidationError(
  #   #     _(f"Project name '{_name}' is already taken, try another one."),
  #   #     code='invalid'
  #   #   )
  #   return name