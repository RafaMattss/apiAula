from rest_framework import serializers
from api.models.student import StudentEntity

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntity
        fields = '__all__'