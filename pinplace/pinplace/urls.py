from django.contrib import admin
from django.urls import path, include

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', include('pins.urls')),
]