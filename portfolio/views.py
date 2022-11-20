from rest_framework.decorators import action
from rest_framework import viewsets
from . import models
from . import serializers


class ProjectsView(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
