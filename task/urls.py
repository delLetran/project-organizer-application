
from django.urls import path
from .views import (
  # test_view,
  task_create_view,
  task_list_view,
  task_details_view,
  task_update_view,
  task_delete_view,
  
)
app_name='task'
urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/task/create/', task_create_view, name="create"),
  path('api/task/list/<int:activity_id>/', task_list_view, name="list"),
  path('api/task/<int:id>/', task_details_view, name="details"),
  path('api/task/<int:id>/update/', task_update_view, name="update"),
  path('api/task/<int:id>/delete/', task_delete_view, name="delete"),
]

