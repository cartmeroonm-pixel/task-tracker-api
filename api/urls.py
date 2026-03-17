from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet
from django.urls import include, path


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]