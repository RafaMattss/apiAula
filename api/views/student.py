from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.student import StudentEntity
from api.serializers.student import StudentSerializer

# Classe que define as visualizações relacionadas aos estudantes.
class StudentView(APIView):

    # Função utilizada para obter um objeto de estudante com base no seu ID.
    def get_object(self, pk):
        try:
            return StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            raise Http404
        
    # Função utilizada para listar todos os estudantes e retorná-los em formato JSON.
    def get(self, request, format=None):
        student = StudentEntity.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    # Função utilizada para criar um novo estudante e retorná-lo em formato JSON.
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# Classe que define as visualizações detalhadas relacionadas aos estudantes.
class StudentDetailView(APIView):

    # Função utilizada para obter um objeto de estudante com base no seu ID.
    def get_object(self, pk):
        try:
            return StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            raise Http404
    
    # Função utilizada para obter detalhes de um estudante específico e retorná-los em formato JSON.
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # Função utilizada para atualizar os detalhes de um estudante específico e retorná-los em formato JSON.
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Função utilizada para deletar um estudante específico.
    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
