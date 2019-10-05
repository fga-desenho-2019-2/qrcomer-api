from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)

    class Meta:
        verbose_name = u'Profile'
        verbose_name_plural = u'Profiles'

    def __str__(self):
        return self.cpf
