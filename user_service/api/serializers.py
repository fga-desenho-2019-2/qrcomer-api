from rest_framework.serializers import ModelSerializer
from user_service.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
