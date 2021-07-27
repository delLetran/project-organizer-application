from django.contrib import admin
from .models import Associate

@admin.register(Associate)
class AssociateAdmin(admin.ModelAdmin):
  list_display = ('sender', 'receiver', 'status')

  def save_model(self, request, obj, form, change):
    if not obj.sender:
      obj.sender = request.user
    obj.save()