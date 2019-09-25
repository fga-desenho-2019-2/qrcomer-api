from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_lenght = 50)
    email = models.EmailField(max_length = 20)