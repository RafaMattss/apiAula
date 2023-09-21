from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.student import StudentEntity
from api.models.task import TaskEntity
from api.serializers.task import TaskSerializer

class TaskStudentView(APIView):

    #Função utilizada para pegar um objeto
    def get_object(self, pk):
        try:
            return StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            raise Http404
        
    #Função utilizada para pegar um objeto filtrando um outro (tarefas associadas a aluno)
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        task = TaskEntity.objects.filter(students=student)  # Ajuste aqui
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)





