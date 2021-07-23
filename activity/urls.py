
from django.urls import path
from .views import (
  # test_view,
  activity_create_view,
  activity_details_view,
  activity_update_view,
  activity_delete_view,
)

# app_name='activity'
urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/activity/create/', activity_create_view, name="activity-create"),
  path('api/activity/<int:id>/', activity_details_view, name="activity-detail"),
  path('api/activity/<int:id>/update/', activity_update_view, name="activity-update"),
  path('api/activity/<int:id>/delete/', activity_delete_view, name="activity-delete"),
]

