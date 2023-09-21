from django.db import models
from api.models.student import StudentEntity
from api.models.discipline import DisciplineEntity

class TaskEntity(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    issue_date = models.DateField()
    completed = models.BooleanField()
    students = models.ForeignKey(StudentEntity, on_delete=models.CASCADE) #Função on_delete faz com que se eu delete um objeto, o outro associado a ele também será deletado
    disciplines = models.ManyToManyField(DisciplineEntity)

