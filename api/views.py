from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    search_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["get"], url_path="tasks")
    def tasks(self, request, pk=None):
        project = self.get_object()
        queryset = project.tasks.filter(owner=request.user).order_by("-id")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TaskSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = TaskSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filterset_fields = ['project', 'status']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
