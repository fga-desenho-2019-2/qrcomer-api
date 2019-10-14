from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# from django.contrib.auth.models import UserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, cpf, password, birth_date, sex, first_name, last_name):
        if not email:
            raise ValueError('User must have an Email')
        if not password:
            raise ValueError('User must have a Password')
        if not cpf:
            raise ValueError('User must have a CPF')
        if not birth_date:
            raise ValueError('User must have a birth day')
        if not sex:
            raise ValueError('User must have a gender')
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name:
            raise ValueError('User must have a last name')

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
        if not email:
            raise ValueError('User must have an Email')
        if not password:
            raise ValueError('User must have a Password')
        if not cpf:
            raise ValueError('User must have a CPF')
        if not birth_date:
            raise ValueError('User must have a birth day')
        if not sex:
            raise ValueError('User must have a gender')
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name:
            raise ValueError('User must have a last name')

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
    password = models.CharField(max_length=128, verbose_name='password')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150)
    sex = models.CharField(max_length=1)
    birth_date = models.DateField()
    is_staff = models.BooleanField(default=False)
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
