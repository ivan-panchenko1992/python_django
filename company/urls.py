from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'workers', ItemViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]