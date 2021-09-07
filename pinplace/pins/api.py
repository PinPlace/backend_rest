from pins.models import Pins, Lists
from rest_framework import viewsets, permissions
from .serializers import PinsSerializer, ListsSerializer

# Pin Viewset - create full CRUD API without explicitly declaring method functionality
class PinsViewSet(viewsets.ModelViewSet):
    queryset = Pins.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PinsSerializer

class ListsViewSet(viewsets.ModelViewSet):
    queryset = Lists.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListsSerializer