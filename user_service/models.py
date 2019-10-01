from django.db import models
from django.conf import settings

class Client(models.Model):

    registro = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=400)
    cpf = models.CharField(max_length = 14)


    def __str__(self):
        return self.first_name + self.last_name