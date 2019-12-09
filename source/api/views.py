from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly

from .serializers import TaskSerializer, ProjectSerializer
from webapp.models import Task, Project


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

#
# class OrderProductViewSet(viewsets.ModelViewSet):
#     serializer_class = OrderProductSerializer
#     queryset = OrderProduct.objects.all()
