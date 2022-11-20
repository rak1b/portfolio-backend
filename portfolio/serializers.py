from .models import *
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.ReadOnlyField(source="tags_list")

    class Meta:
        model = Project
        fields = "__all__"
