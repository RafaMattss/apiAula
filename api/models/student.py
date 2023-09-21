from django.db import models

class StudentEntity(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return "Student [%i - %s -%e]" % (self.id, self.name, self.email)