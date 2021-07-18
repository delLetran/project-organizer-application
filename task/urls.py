
from django.urls import path
from .views import (
  # test_view,
  task_create_view,
)

urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/task/create/', task_create_view, name="task-create"),
]

