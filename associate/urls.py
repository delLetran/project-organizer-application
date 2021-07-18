
from django.urls import path
from .views import (
  # test_view,
  user_associates_list_view,
  user_mutual_associates_list_view,
  # user_mutual_associates_detail_view,
)

urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/associate/list/', user_associates_list_view, name="associate-list"),

  path('api/associate/mutual/', user_mutual_associates_list_view, name="associate-mutual-list"),
  # path('api/associates/mutual/<str:username>/', user_mutual_associates_detail_view, name="associates-mutual"),

]
