from rest_framework import serializers
from ..models import Profile
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Profile(
            email=validated_data["email"],
            cpf=validated_data["cpf"],
            birth_date=validated_data['birth_date'],
            sex=validated_data['sex']

        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'profile' in validated_data:
            instance.user.password = make_password(
                validated_data.get('profile').get('password', instance.user.password)
            )
            instance.profile.save()

    class Meta:
        model = Profile
        fields = ['id', 'cpf', 'first_name', 'last_name', 'birth_date', 'sex', 'email', 'password']
        read_only_fields = ['date_joined', 'last_login', 'user_permissions', 'groups', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}