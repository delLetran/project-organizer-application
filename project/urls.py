
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

app_name='project'
urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/project/create/', project_create_view, name="create"),
  path('api/project/list/', project_list_view, name="list"),
  # path('api/project/create-form/', project_create_form_view, name="create-form"),
  path('api/project/<str:slug>/', project_details_view, name="details"),
  path('api/project/<str:slug>/update/', project_update_view, name="update"),
  path('api/project/<str:slug>/delete/', project_delete_view, name="delete"),
]
