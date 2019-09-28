from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    username = None

    first_name = models.TextField(max_length = 50)

    last_name = models.TextField(max_length = 50)

    email = models.EmailField(unique=True)

    cpf = models.CharField(primary_key = True, max_length = 14)

    def __str__(self):
        return self.first_name + self.last_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
