from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet
# from users.views import registration_view

# app_name = 'users'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('register/', registration_view, name="register"),
]