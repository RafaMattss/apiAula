from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.discipline import DisciplineEntity
from api.serializers.discipline import DisciplineSerializer

# Classe que define as visualizações relacionadas às disciplinas.
class DisciplineView(APIView):

    # Função utilizada para obter um objeto de disciplina com base no seu ID.
    def get_object(self, pk):
        try:
            return DisciplineEntity.objects.get(pk=pk)
        except DisciplineEntity.DoesNotExist:
            raise Http404
        
    # Função utilizada para listar todas as disciplinas e retorná-las em formato JSON.
    def get(self, request, format=None):
        discipline = DisciplineEntity.objects.all()
        serializer = DisciplineSerializer(discipline, many=True)
        return Response(serializer.data)

    # Função utilizada para criar uma nova disciplina e retorná-la em formato JSON.
    def post(self, request, format=None):
        serializer = DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    
# Classe que define as visualizações detalhadas relacionadas às disciplinas.
class DisciplineDetailView(APIView):
    
    # Função utilizada para obter um objeto de disciplina com base no seu ID.
    def get_object(self, pk):
        try:
            return DisciplineEntity.objects.get(pk=pk)
        except DisciplineEntity.DoesNotExist:
            raise Http404
    
    # Função utilizada para obter detalhes de uma disciplina específica e retorná-los em formato JSON.
    def get(self, request, pk, format=None):
        discipline = self.get_object(pk)
        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data)
    
    # Função utilizada para atualizar os detalhes de uma disciplina específica e retorná-los em formato JSON.
    def put(self, request, pk, format=None):
        discipline = self.get_object(pk)
        serializer = DisciplineSerializer(discipline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Função utilizada para deletar uma disciplina específica.
    def delete(self, request, pk, format=None):
        discipline = self.get_object(pk)
        discipline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
