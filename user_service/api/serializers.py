from rest_framework.serializers import ModelSerializer
from user_service.models import Profile
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'first_name', 'username', 'email']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['cpf']
