from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Item, Task
from .serializers import ItemCreateSerializer, ItemUpdateSerializer, TaskCreateSerializer, TaskUpdateSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return ItemCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ItemUpdateSerializer
        return ItemCreateSerializer
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return TaskUpdateSerializer
        return TaskCreateSerializer

    @action(detail=False, methods=['get'], url_path='high-estimate')
    def high_estimate(self, request):
        passed_estimate = request.query_params.get('estimate')
        try:
            passed_estimate = int(passed_estimate)
            if passed_estimate < 0:
                raise ValueError("Estimate must be a non-negative integer")
        except ValueError:
            return Response({"error": "Estimate must be a valid non-negative integer"}, status=400)

        high_estimate_tasks = self.queryset.filter(estimate__gt=passed_estimate)
        serializer = self.get_serializer(high_estimate_tasks, many=True)
        return Response(serializer.data)