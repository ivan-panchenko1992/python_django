from rest_framework import viewsets
from .models import Item
from .serializers import ItemCreateSerializer, ItemUpdateSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return ItemCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ItemUpdateSerializer
        return ItemCreateSerializer