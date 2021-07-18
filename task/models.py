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
ACTIVITY =  'activity.Activity'
    
class Task(models.Model):
  class IMPORTANCE(models.IntegerChoices):  
    VLO = 1, _('Very Low'),
    LOW = 2, _('Low'),
    MED = 3, _('Medium'), 
    HI = 4, _('High'),
    VHI = 5, _('Very High')

  PATCH_CHOICES = [ 
    (1001, _('DASHED01')),
    (1002, _('DASHED02')),
    (1003, _('DASHED03')),
    (1004, _('DASHED04')),
    (1005, _('DASHED05')),
    (2001, _('DOTTED01')),
    (2002, _('DOTTED02')),
    (2003, _('DOTTED03')),
    (2004, _('DOTTED04')),
    (2005, _('DOTTED05')),
    (3001, _('SOLID01') ),
    (3002, _('SOLID02') ),
    (3003, _('SOLID03') ), 
    (3004, _('SOLID04') ), 
    (3005, _('SOLID05') )
  ]

  name = models.CharField(max_length=MAX_LENGTH_NAME)
  desciption = models.CharField(max_length=MAX_LENGTH_DESC, blank=True, null=True)
  start_date = models.DateField(_("task start date"), auto_now=False, auto_now_add=False, blank=True, null=True)
  due_date = models.DateField(_("task due date"), auto_now=False, auto_now_add=False, blank=True, null=True)
  created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
  importance = models.PositiveSmallIntegerField(choices=IMPORTANCE.choices, default=IMPORTANCE.MED)
  patch = models.PositiveSmallIntegerField(_("task line & color marking(patch)"), choices=PATCH_CHOICES, blank=True, null=True)
  activity = models.ForeignKey(ACTIVITY, default=2, on_delete=models.CASCADE)
  created_by = models.ForeignKey(USER, on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if not self.patch:
      self.patch = random.choices(Task.PATCH_CHOICES)[0][0]
    return super(Task, self).save(*args, **kwargs)

@receiver(post_save, sender=Task)
def post_save_task(sender, instance, created, *args, **kwargs):
  _created_by = instance.created_by
  _activity = instance.activity
  # _activity = None
  # if instance.activity:
  #   _activity = instance.activity
  # pk = 'pass in task creator here'
  # member = _activity.project.members.filter(USER.objects.get(pk=pk))
  # is_member =member.exists()
  if created:
    if _created_by == _activity.created_by:
      _activity.tasks.add(instance)
    # if _activity != None :
        
    # # elif is_member:
    #   # add  if for member has permissions to add a task (such as project_admin, manager, and alike)
    #   else:
    #     _activity.tasks.add(instance)
    #     print('activity task must be created under an Activity')
    # else:
    #   print('will return => error: you don\'t have permission to add task to this activity')
    
