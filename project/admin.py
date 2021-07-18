from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name','slug','created_by','description')

  def save_model(self, request, obj, form, change):
    if not obj.created_by:
      obj.created_by = request.user
    obj.save()
