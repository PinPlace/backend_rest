from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include('users.urls', namespace='user-views')),
    path('admin/', admin.site.urls),
    path('', include('pins.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token-verify/', TokenVerifyView.as_view(), name='token_verify')
]