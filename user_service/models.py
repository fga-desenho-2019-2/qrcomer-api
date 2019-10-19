from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# from django.contrib.auth.models import UserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, cpf, password, birth_date, sex, first_name, last_name):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.cpf = cpf
        user.birth_date = birth_date
        user.sex = sex
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, password, birth_date, sex, first_name, last_name):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.cpf = cpf
        user.birth_date = birth_date
        user.sex = sex
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class Profile(AbstractBaseUser, PermissionsMixin):

    cpf = models.CharField(unique=True, max_length=11)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=1)
    birth_date = models.DateField(verbose_name='data de nascimento')
    is_staff = models.BooleanField(default=False, verbose_name='administrador')
    is_superuser = models.BooleanField(default=False, verbose_name='superusuario')
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'first_name', 'last_name', 'sex', 'birth_date']

    objects = CustomUserManager()

    class Meta:
        verbose_name = u'Profile'
        verbose_name_plural = u'Profiles'

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email


class Card(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    number = models.CharField(unique=True, primary_key=True, max_length=16, blank=False)
    cvv = models.CharField(blank=False, null=False, max_length=3)
    validation = models.DateField(verbose_name='Validade')
    holder_name = models.CharField(max_length=30, blank=False)
    cpf_cnpj = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = u'Card'
        verbose_name_plural = u'Cards'

    def __str__(self):
        return self.number