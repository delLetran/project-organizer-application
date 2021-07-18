from django.contrib import admin
from collaborator.models import Collaborator

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
  list_display = ('project', 'name', 'inviter', 'position', 'status' )

  def save_model(self, request, obj, form, change):
    if not obj.inviter:
      obj.inviter = request.user
    obj.save()