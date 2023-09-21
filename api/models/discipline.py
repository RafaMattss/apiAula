from django.db import models

class DisciplineEntity(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()