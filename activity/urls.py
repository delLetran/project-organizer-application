
from django.urls import path
from .views import (
  # test_view,
  activity_create_view,
  activity_details_view,
)

urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/activity/create/', activity_create_view, name="activity-create"),
  path('api/activity/<int:id>/', activity_details_view, name="activity-detail"),
]

