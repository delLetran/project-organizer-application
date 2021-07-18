from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('name', 'desciption', 'importance', 'activity' )

  def save_model(self, request, obj, form, change):
    if not obj.created_by:
      obj.created_by = request.user
    obj.save()
