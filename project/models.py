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
from collaborator.models import Collaborator
ACTIVITY = 'activity.Activity'
PROJECTACTIVITY = 'activity.ProjectActivity'
COLLABORATOR = 'collaborator.Collaborator'
# NOTE = 'activity.Note'



class Project(models.Model):
  class TYPE(models.IntegerChoices):
    SOFTDEV = 2, _('Software Development'),
    EQUIP = 3, _('Equipment / System Installation')

  class STATUS(models.IntegerChoices):
    PO = 1, _('Ongoing'),
    PH = 2, _('On-Hold'),
    PC = 3, _('Completed'),
    PD = 4, _('Delivered')

  name = models.CharField(max_length=MAX_LENGTH_NAME)
  slug = models.CharField(_("project_name_slug"), max_length=MAX_LENGTH_NAME, blank=True, null=True)
  description = models.TextField(max_length=MAX_LENGTH_DESC, blank=True, null=True)
  created_by = models.ForeignKey(USER, related_name='created_by', blank=True, null=True, on_delete=models.CASCADE)
  status =  models.PositiveSmallIntegerField(_("project status"), default=STATUS.PO, choices=STATUS.choices)
  project_type =  models.PositiveSmallIntegerField(_("project type"), default=TYPE.SOFTDEV, choices=TYPE.choices)
  # collaborators = models.ManyToManyField( USER, through=COLLABORATOR, through_fields=('project', 'name'), default=[0])
  collaborators = models.ManyToManyField(COLLABORATOR, related_name='collaborator', verbose_name=_("collaborator"), blank=True)
  activities = models.ManyToManyField(ACTIVITY, related_name='activity', verbose_name=_("activity"), blank=True)
  # notes = models.ManyToManyField(NOTE, related_name='note', verbose_name=_("note"), blank=True, null=True)

  # activities = models.ManyToManyField( ACTIVITY, through='PROJECTACTIVITY', through_fields=('project', 'activity'))

  # requirments = models.OneToOneField(REQUIREMENT, on_delete=models.CASCADE, blank=True, null=True)
  # schedlule = models.ForeignKey(SCHEDULE, on_delete=models.CASCADE, blank=True, null=True)
  # requirment = models.ManyToManyField(REQUIREMENT, blank=True, default=[0])
  # progress = models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

  class Meta:
    ordering = ['-pk']
    unique_together = ['name', 'created_by']
  
  def save(self, *args, **kwargs):
    _suffix = str(self.created_by.id) + (get_random_string(3,'0123456789'))
    slug_suffix = (urlsafe_base64_encode(force_bytes(_suffix)))
    self.slug = slugify(f'{self.name}_{slug_suffix}')
    super(Project, self).save(*args, **kwargs)

  def add_collaborator(self, name, position=4):
    collaborator = Collaborator(
      project=self,
      name=name,
      inviter=self.created_by,
      position=position
    )
    collaborator.save()

  def __str__(self):
    return self.name

@receiver(post_save, sender=Project)
def post_save_project(sender, instance, created, position=1, *args, **kwargs):
  _user = instance.created_by
  if created:
    _user.projects.add(instance)
    Collaborator.objects.create(
      project=instance,
      name=instance.created_by,
      inviter=instance.created_by,
      position=position
    )













# @receiver(post_save, sender=Collaborator)
# def post_save_project_group(sender, instance, created, *args, **kwargs):
#   _sender = instance.inviter
#   _receiver = instance.collaborator
#   _status = instance.status
#   if not created:
#     if _status == 'Joined':

    # if _status =='Leave':
    #   if _status =='Declined' :
    #   if _status =='Invited' :
  



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
