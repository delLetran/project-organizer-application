
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('project.urls')),
    path('', include('collaborator.urls')),
    path('', include('activity.urls')),
    path('', include('task.urls')),
    path('', include('associate.urls')),
]
