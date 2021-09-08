from rest_framework import routers
from pins.api import PinsViewSet, ListsViewSet

app_name ="pins"

router = routers.DefaultRouter()
router.register('api/pins', PinsViewSet, 'pins_router')
router.register('api/lists', ListsViewSet, 'list_router')

urlpatterns = router.urls