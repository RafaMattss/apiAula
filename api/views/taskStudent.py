from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.student import StudentEntity
from api.models.task import TaskEntity
from api.serializers.task import TaskSerializer

# Classe que define visualizações relacionadas a tarefas associadas a um aluno.
class TaskStudentView(APIView):

    # Função utilizada para obter um objeto de aluno com base no seu ID.
    def get_object(self, pk):
        try:
            return StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            raise Http404
        
    # Função utilizada para obter tarefas associadas a um aluno específico.
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        
        # Filtra as tarefas com base no aluno específico (tarefas associadas a esse aluno).
        task = TaskEntity.objects.filter(students=student)
        
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
