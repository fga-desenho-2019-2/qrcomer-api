from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone


class Profile(AbstractBaseUser):

    cpf = models.CharField(unique=True, max_length=11, primary_key=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf']

    class Meta:
        verbose_name = u'Profile'
        verbose_name_plural = u'Profiles'

    def __str__(self):
        return self.cpf
