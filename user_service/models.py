from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    first_name = models.CharField(blank = True, max_length = 50)

    last_name = models.CharField(blank = True, max_length = 50)

    email = models.EmailField()

    cpf = models.CharField(blank = True, max_length = 14)

    EMAIL_FIELD = ['email']
    REQUIRED_FIELDS = ['email']