from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserViewSet, AuthViewSet
# from django.contrib.auth import views as auth_views
# from users.views import registration_view

app_name = 'users'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/register/', AuthViewSet.as_view({'post': 'create'}), name='register_user'),
    # path('users/login/', TokenObtainPairView.as_view(), name='access_tokem'),
    # path('users/refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),
    # path('users/token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('register/', registration_view, name="register"),
]