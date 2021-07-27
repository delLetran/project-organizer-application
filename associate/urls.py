
from django.urls import path
from .views import (
  invite_view,
  accept_invite_view,
  decline_invite_view,
  cancel_invite_view,
  dissociate_view,
  sent_invites_view,
  received_invites_view,

  list_view,
  mutual_list_view,
  user_mutual_list_view,
)
app_name='associate'
urlpatterns = [
  path('api/associate/<str:invitee>/invite/', invite_view, name="invite"),
  path('api/associate/<str:inviter>/accept/', accept_invite_view, name="accept"),
  path('api/associate/<str:inviter>/decline/', decline_invite_view, name="decline"),
  path('api/associate/<str:invitee>/cancel/', cancel_invite_view, name="cancel"),
  path('api/associate/<str:associate>/dissociate/', dissociate_view, name="dissociate"),
  path('api/associate/sent-invites/', sent_invites_view, name="sent-invites"),
  path('api/associate/received-invites/', received_invites_view, name="received-invites"),
  path('api/associate/list/', list_view, name="list"),
  path('api/associate/mutual-list/', mutual_list_view, name="mutual-list"),
  path('api/associate/mutual/<str:username>/', user_mutual_list_view, name="user-mutual-list"),
  # path('api/associates/mutual/<str:username>/', user_mutual_associates_detail_view, name="associates-mutual"),

]