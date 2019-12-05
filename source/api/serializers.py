from rest_framework import serializers
from webapp.models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'brief', 'description', 'status', 'type', 'project', 'created_at', 'updated_at', 'created_by')


class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'project_name', 'description', 'created_at', 'updated_at','tasks')


