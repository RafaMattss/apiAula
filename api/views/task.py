from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.task import TaskEntity
from api.serializers.task import TaskSerializer

class TaskView(APIView):

    #Função utilizada para pegar um objeto
    def get_object(self, pk):
        try:
            return TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            raise Http404
        
    #Função utilizada para pegar todos objetos e retorná-los em Json
    def get(self, request, format=None):
        task = TaskEntity.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    #Função utilizada para criar um objeto e retorná-lo em Json  
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class TaskDetailView(APIView):

    #Função utilizada para pegar um objeto
    def get_object(self, pk):
        try:
            return TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            raise Http404

    #Função utilizada para pegar um objeto e retorná-lo em Json    
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    #Função utilizada para atualizar um objeto e retorná-lo em Json 
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Função utilizada para deletar um objeto
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)