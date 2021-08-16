
from django.urls import path
from .views import (
  get_project_collaborators_view,
  invite_view,
  remove_collaborator_view,
  cancel_invite_view,
  accept_invite_view,
  decline_invite_view,
  leave_project_view,
  update_collaborator_position_view,
  sent_invites_view,
  received_invites_view,
)

app_name='collaborator'
urlpatterns = [
  path('api/collaborator/<int:project_id>/', get_project_collaborators_view, name="list"),
  path('api/collaborator/<str:invitee>/<int:project_id>/invite/', invite_view, name="invite"),
  path('api/collaborator/<str:collaborator>/<int:project_id>/remove/', remove_collaborator_view, name="remove"),
  path('api/collaborator/<str:invitee>/<int:project_id>/cancel/', cancel_invite_view, name="cancel"),
  path('api/collaborator/<int:project_id>/accept/', accept_invite_view, name="accept"),
  path('api/collaborator/<int:project_id>/decline/', decline_invite_view, name="decline"),
  path('api/collaborator/<int:project_id>/leave/', leave_project_view, name="leave"),
  path('api/collaborator/<int:collaborator_id>/update/', update_collaborator_position_view, name="update"),
  path('api/collaborator/sent-invites/', sent_invites_view, name="sent-invites"),
  path('api/collaborator/received-invites/', received_invites_view, name="received-invites"),
]
