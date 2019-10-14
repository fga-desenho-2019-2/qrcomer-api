from rest_framework import serializers
from ..models import Profile
# from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['date_joined', 'last_login', 'user_permissions', 'groups']