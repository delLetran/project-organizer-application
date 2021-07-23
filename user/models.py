from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
  AbstractUser,
  AbstractBaseUser,
  PermissionsMixin,
  BaseUserManager
)
from django.utils.translation import ugettext_lazy as _

PROJECT = 'project.Project'


class CustomUserManager(BaseUserManager): 
  def create_superuser(self, email, username, first_name, last_name, password, **kwargs):
    kwargs.setdefault('is_staff', True)
    kwargs.setdefault('is_superuser', True)
    kwargs.setdefault('is_active', True)

    if kwargs.get('is_staff') is not True:
      raise ValueError('is_staff must be set True for superuser')
    if kwargs.get('is_superuser') is not True:
      raise ValueError('is_superuser must be set True for superuser')
    return self.create_user(email, username, first_name, last_name, password, **kwargs)

  def create_user(self, email, username, first_name, last_name, password, **kwargs):
    return self._create_user(email, username, first_name, last_name, password, **kwargs)

  def _create_user(self, email, username, first_name, last_name, password, **kwargs):
    if not email:
      raise ValueError(_('Enter a valid email address'))
    email = self.normalize_email(email)
    user = self.model(
      email=email,
      username=username,
      first_name=first_name,
      last_name=last_name,
      **kwargs
    )
    user.set_password(password)
    user.save()
    return user

    
  def is_owner(self, request, username):
    return request.user.username == username

class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_('email address'), max_length=60, unique=True)
  username = models.CharField( max_length=60, unique=True)
  first_name = models.CharField(max_length=60, blank=True, null=True)
  last_name = models.CharField(max_length=60, blank=True, null=True)
  about = models.TextField(_("about"), max_length=512, blank=True, null=True)
  start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  birth_date = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False, blank=True, null=True)
  job_title = models.CharField(max_length=50, blank=True, null=True)
  projects = models.ManyToManyField(PROJECT, verbose_name=_("projects"), related_name='project_list', blank=True)
  associates = models.ManyToManyField('CustomUser', verbose_name=_("associates"), blank=True)
  joined_projects = models.ManyToManyField(PROJECT, verbose_name=_("projects joined"), related_name='joined_projects', default=[0], blank=True)
   
  objects = CustomUserManager()

  USERNAME_FIELD = ('email')
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  def get_associates(self):
    return self.associates.all()

  def get_associates_id(self):
    assocs = self.get_associates()
    assocs_id = []
    for assoc in assocs:
      assocs_id.append(assoc.id)
    return assocs_id

  def get_mutual_associates(self, profile):
    user_assocs = self.get_associates_id()
    profile_assocs = profile.get_associates_id()
    mutual_assocs = list(set(user_assocs).intersection(profile_assocs))
    return mutual_assocs
    
  def get_mutual_associates_details(self, profile):
    mutual_assocs = self.get_mutual_associates(profile)
    return CustomUser.objects.filter(pk__in=mutual_assocs)
    
  def get_associate_with_mutual_associates_list(self):
    user_assocs = self.get_associates()
    mutual_associates = []
    for user_assoc in user_assocs:
      profile_list = self.get_mutual_associates_details(user_assoc)
      if len(profile_list) >= 1:
        mutual_associates.append((user_assoc, profile_list))
    return mutual_associates
    
  def __str__(self):
    return self.username

  class Meta:
    ordering = ['username', '-pk',]
    db_table = 'auth_user' 
    managed = True 
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'

 