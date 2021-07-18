
from django.urls import path
from .views import (
  # test_view,
  note_create_view,
)

urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/note/create/', note_create_view, name="note-create"),
]

