
from django.urls import path
from .views import (
  # test_view,
  user_signup_view,
  user_activate_view,
  user_resend_email_verification_view,
  user_delete_view,
  user_update_view,
  user_details_view,
  user_update_password_view,
  user_data_view
)

urlpatterns = [
  # path('api/test/', test_view, name="_test_"),
  path('api/signup/', user_signup_view, name="user-signup"),
  path('account-verification/<str:uid>/<str:token>/', user_activate_view, name="user-activate"),
  path('api/user/resend-verification/', user_resend_email_verification_view, name="user-resend-verification"),
  path('api/user/delete/', user_delete_view, name="user-delete"),
  path('api/user/update/', user_update_view, name="user-update"),
  path('api/user/update-password/', user_update_password_view, name="user-update-password"),
  path('api/user/<str:username>/', user_details_view, name="user-details"),
  path('api/user/data/', user_data_view, name="user-data"),
]
