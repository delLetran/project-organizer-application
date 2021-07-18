
from django.urls import path
from .views import (
  # test_view,
  project_details_view,
  project_list_view,
  project_create_view,
  project_update_view,
  project_delete_view,
  # project_create_form_view,
)

urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/project/create/', project_create_view, name="project-create"),
  path('api/project/list/', project_list_view, name="project-list"),
  # path('api/project/create-form/', project_create_form_view, name="project-create-form"),
  path('api/project/<str:slug>/', project_details_view, name="project-details"),
  path('api/project/<str:slug>/update/', project_update_view, name="project-update"),
  path('api/project/<str:slug>/delete/', project_delete_view, name="project-delete"),
]
