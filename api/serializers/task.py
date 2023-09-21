from rest_framework import serializers
from api.models.task import TaskEntity

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEntity
        fields = '__all__'