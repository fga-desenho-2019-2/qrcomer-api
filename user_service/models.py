from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name="user"
    )
    cpf = models.CharField(max_length=14)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)

    class Meta:
        verbose_name = u'Profile'
        verbose_name_plural = u'Profiles'

    def __str__(self):
        return self.cpf
