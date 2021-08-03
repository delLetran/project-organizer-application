from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# from django.contrib.auth import get_user_model

# User = get_user_model()
from .models import CustomUser as User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
  ordering = ('pk', )
  fieldsets = (
    (None, {'fields': ( 'email',  'username','password',)}),
    (_('Personal info'), {'fields': ('first_name', 'last_name', 'birth_date')}),
    (_('Projects '), {'fields': ( 'projects', 'joined_projects')}),
    # (_('Projects '), {'fields': ( 'projects', )}),
    (_('Qualifications'), {'fields': ( 'job_title', 'about')}),
    (_('Associates'), {'fields': ( 'associates', )}),
    (_('Permissions'), {
      'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    }),
    (_('Important dates'), {'fields': ('last_login', 'start_date')}),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email',  'username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')}
    ),
  )
