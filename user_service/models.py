from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    first_name = models.CharField(max_length = 50)

    last_name = models.CharField(max_length = 50)

    email = models.EmailField()

    cpf = models.CharField(primary_key = True, max_length = 14)

    def __str__(self):
        return self.first_name + self.last_name
    
    EMAIL_FIELD = ['email']
    REQUIRED_FIELDS = ['email']
    