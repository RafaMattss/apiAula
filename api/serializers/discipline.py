# api/serializers.py
from rest_framework import serializers
from api.models.discipline import DisciplineEntity

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineEntity
        fields = '__all__'