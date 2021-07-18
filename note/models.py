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



class Note(models.Model):
  tag = models.CharField(_("note tag"), max_length=MAX_LENGTH_NAME)
  description = models.TextField(_("note description"), max_length=MAX_LENGTH_TEXT)
  project = models.ForeignKey(PROJECT, on_delete=models.CASCADE)
  created_by = models.ForeignKey(USER, related_name='note_created_by', blank=True, null=True, on_delete=models.CASCADE)
    
  class Meta:
    verbose_name = _("Note")
    verbose_name_plural = _("Notes")

  def __str__(self):
    return self.tag

@receiver(post_save, sender=Note)
def post_save_note(sender, instance, created, *args, **kwargs):
  _project = instance.project
  
  _created_by = instance.created_by
  if created:
    if _created_by == _project.created_by:
      _project.note.add(instance)