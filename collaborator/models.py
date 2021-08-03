from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
from django.utils.crypto import get_random_string

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

MAX_LENGTH_NAME = settings.MAX_LENGTH_NAME
MAX_LENGTH_USERNAME = settings.MAX_LENGTH_USERNAME
MAX_LENGTH_JOB = settings.MAX_LENGTH_JOB
MAX_LENGTH_DESC = settings.MAX_LENGTH_DESC
MAX_LENGTH_TEXT = settings.MAX_LENGTH_TEXT
MAX_LENGTH_CHOICES = settings.MAX_LENGTH_CHOICES

USER = get_user_model()
PROJECT = 'project.Project'


class Collaborator(models.Model): 
  class POSITION(models.IntegerChoices):
    PAD = 1, _('Project Admin'),
    PMA = 2, _('Project Manager'),
    PLE = 3, _('Project Leader'), 
    MEM = 4, _('Member'),
    SPE = 5, _('Spectator')

  class STATUS(models.TextChoices):
    ONHOLD = 'Invited', 
    JOINED = 'Joined',
    LEAVED = 'Leaved',
    REMOVED = 'Removed',
    DECLINED = 'Declined'

  name = models.ForeignKey(USER, related_name='collaborator', on_delete=models.CASCADE)
  project = models.ForeignKey(PROJECT, on_delete=models.CASCADE)
  position = models.PositiveSmallIntegerField(choices=POSITION.choices, default=POSITION.MEM)
  inviter = models.ForeignKey(USER, related_name='group_invites', on_delete=models.CASCADE, blank=True, null=True)
  is_active = models.BooleanField(_("invite_active"), default=True)
  status = models.CharField(_("invite status"), max_length=MAX_LENGTH_NAME, choices=STATUS.choices, default=STATUS.ONHOLD)
  # permission_1 = models.BooleanField(_("manager_permission"), default=False)
  # permission_2 = models.BooleanField(_("accounting_permission"), default=False)
  # permission_3 = models.BooleanField(_("document_permission"), default=True)

  class Meta:
    # unique_together = ['name', 'project']
    verbose_name = _("Collaborator")
    verbose_name_plural = _("Collaborators")

  def __str__(self):
    return f'{self.name} @ {self.project}'

  def accept_collaboration_invite(self):
    self.status = self.STATUS.JOINED
    self.save()
    return self.status

  def decline_collaboration_invite(self):
    self.status = self.STATUS.DECLINED
    self.save()
    return self.status

  def cancel_collaboration_invite(self):
    self.status = self.STATUS.REMOVED
    self.save()
    return self.status

  def remove_collaborator(self):
    self.status = self.STATUS.REMOVED
    self.save()
    return self.status

  def leave_project(self):
    self.status = self.STATUS.LEAVED
    self.save()
    return self.status

 
@receiver(pre_save, sender=Collaborator)
def pre_save_project_collaborator(sender, instance, *args, **kwargs):
  _receiver = instance.name
  _project = instance.project
  _status = instance.status
  if _project.created_by == _receiver:
    instance.status = 'Joined'
    # _project.collaborators.add(instance)

  if _status == 'Joined' or _status =='Leaved' or _status =='Removed'  or _status =='Declined':
    instance.is_active = False
  elif _status == 'Invited':
    instance.is_active = True
    

@receiver(post_save, sender=Collaborator)
def post_save_project_collaborator(sender, instance, created, *args, **kwargs):
  _sender = instance.inviter
  _receiver = instance.name
  _project = instance.project
  _status = instance.status
  if created:
    if _project.created_by == _receiver:
      _project.collaborators.add(instance)
      
  if not created:
    if _project.created_by == _receiver:
      if _status == 'Joined':
        _project.collaborators.add(instance)

    if not _project.created_by == _receiver:
      if _status == 'Joined':
        _project.collaborators.add(instance)
        _receiver.joined_projects.add(_project)
      elif _status =='Leaved':
        _project.collaborators.remove(instance)
        _receiver.joined_projects.remove(_project)
        instance.delete()
      elif _status =='Removed':
        _project.collaborators.remove(instance)
        _receiver.joined_projects.remove(_project)
        instance.delete()
      elif _status =='Declined':
        _project.collaborators.remove(instance)
        _receiver.joined_projects.remove(_project)
        instance.delete()



# @receiver(pre_save, sender=Project)
# def pre_save_project(sender, instance, *args, **kwargs): 
#   print('added: ', instance.admin.all())

# @receiver(post_save, sender=Project)
# def post_save_project(sender, instance, created, *args, **kwargs):
#   if not created:
#     instance.admin.set([instance.created_by])

# @receiver(m2m_changed, sender=Project.admin.through)
# def user_admin_change(sender, instance, action, *args, **kwargs):
#   if action == 'post_add':
#     if not (instance.admin.all().filter(pk=_created_by.pk).exists()):
#       instance.admin.add(_created_by)
