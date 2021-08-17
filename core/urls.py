
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include('user.urls')),
    path('', include('project.urls')),
    path('', include('collaborator.urls')),
    path('', include('activity.urls')),
    path('', include('task.urls')),
    path('', include('associate.urls')),
]
