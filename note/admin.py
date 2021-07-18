from django.contrib import admin
from .models import Activity
# import random

# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#   list_display = ('tag', 'description', 'project')

#   def save_model(self, request, obj, form, change):
#     if not obj.created_by:
#       obj.created_by = request.user
#     obj.save()

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
  list_display = ('name', )

  def save_model(self, request, obj, form, change):
    if not obj.created_by:
      obj.created_by = request.user
    obj.save()