from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

import random

MAX_LENGTH_NAME = settings.MAX_LENGTH_NAME
MAX_LENGTH_USERNAME = settings.MAX_LENGTH_USERNAME
MAX_LENGTH_JOB = settings.MAX_LENGTH_JOB
MAX_LENGTH_DESC = settings.MAX_LENGTH_DESC
MAX_LENGTH_TEXT = settings.MAX_LENGTH_TEXT
MAX_LENGTH_CHOICES = settings.MAX_LENGTH_CHOICES

USER = get_user_model()
PROJECT =  'project.Project'
TASK =  'task.Task'
# PROJECTMEMBER =  'project.ProjectMember'

class Activity(models.Model):
  class STATUS(models.IntegerChoices):
    AO = 1, _('Ongoing'),
    AH = 2, _('On-Hold'),
    AC = 3, _('Completed'),
    AA = 4, _('Abolish ')

  name = models.CharField(_("activity"), max_length=MAX_LENGTH_NAME)
  # summary = models.TextField(_("summary"), max_length=MAX_LENGTH_TEXT, blank=True, null=True)
  status =  models.PositiveSmallIntegerField(_("status"), default=STATUS.AO, choices=STATUS.choices)
  progress = models.SmallIntegerField(_("overall progress"), blank=True, null=True)
  tasks = models.ManyToManyField(TASK, related_name='tasks', verbose_name=_("task"), blank=True)
  project = models.ForeignKey(PROJECT, default=2, on_delete=models.CASCADE)
  created_by = models.ForeignKey(USER, on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    unique_together = ['name', 'project']
    verbose_name = _("Activity")
    verbose_name_plural = _("Activities")

  def __str__(self):
    return self.name

@receiver(post_save, sender=Activity)
def post_save_activity(sender, instance, created, *args, **kwargs):
  _project = instance.project
  _created_by = instance.created_by
  if created:
    if _created_by == _project.created_by:
      _project.activities.add(instance)
    
# @receiver(post_save, sender=Task)
# def post_save_task(sender, instance, created, *args, **kwargs):
#   _created_by = instance.created_by
#   _activity = instance.activity
#   # _activity = None
#   # if instance.activity:
#   #   _activity = instance.activity
#   # pk = 'pass in task creator here'
#   # member = _activity.project.members.filter(USER.objects.get(pk=pk))
#   # is_member =member.exists()
#   if created:
#     if _created_by == _activity.created_by:
#       _activity.tasks.add(instance)
#     # if _activity != None :
        
#     # # elif is_member:
#     #   # add  if for member has permissions to add a task (such as project_admin, manager, and alike)
#     #   else:
#     #     _activity.tasks.add(instance)
#     #     print('activity task must be created under an Activity')
#     # else:
#     #   print('will return => error: you don\'t have permission to add task to this activity')
    

# class ActivitySchedule(models.Model):
#   #Activity(all task)
#   #
    

#   class Meta:
#     verbose_name = _("Schedule")
#     verbose_name_plural = _("Schedules")

#   def __str__(self):
#     return self.name

# @receiver(post_save, sender=Activity)
# def post_save_receiver(sender, **kwargs):
#   # get activity(Tasks)
#   # calculate task duration       
#   pass




# class Note(models.Model):
#   tag = models.CharField(_("note tag"), max_length=MAX_LENGTH_NAME)
#   description = models.TextField(_("note desctiption"), max_length=MAX_LENGTH_TEXT)
#   project = models.ForeignKey(PROJECT, on_delete=models.CASCADE)
#   created_by = models.ForeignKey(USER, related_name='note_created_by', blank=True, null=True, on_delete=models.CASCADE)
    
#   class Meta:
#     verbose_name = _("Note")
#     verbose_name_plural = _("Notes")

#   def __str__(self):
#     return self.tag

# @receiver(post_save, sender=Note)
# def post_save_note(sender, instance, created, *args, **kwargs):
#   _project = instance.project
  
#   _created_by = instance.created_by
#   if created:
#     if _created_by == _project.created_by:
#       _project.note.add(instance)