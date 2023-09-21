from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.task import TaskEntity
from api.serializers.task import TaskSerializer

# Classe que define as visualizações relacionadas às tarefas.
class TaskView(APIView):

    # Função utilizada para obter um objeto de tarefa com base no seu ID.
    def get_object(self, pk):
        try:
            return TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            raise Http404
        
    # Função utilizada para listar todas as tarefas e retorná-las em formato JSON.
    def get(self, request, format=None):
        task = TaskEntity.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    # Função utilizada para criar uma nova tarefa e retorná-la em formato JSON.
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Classe que define as visualizações detalhadas relacionadas às tarefas.
class TaskDetailView(APIView):

    # Função utilizada para obter um objeto de tarefa com base no seu ID.
    def get_object(self, pk):
        try:
            return TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            raise Http404

    # Função utilizada para obter detalhes de uma tarefa específica e retorná-los em formato JSON.
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    # Função utilizada para atualizar os detalhes de uma tarefa específica e retorná-los em formato JSON.
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Função utilizada para deletar uma tarefa específica.
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
