from rest_framework import serializers
from ..models import Profile, Card
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'


class UserCardSerializer(serializers.ModelSerializer):

    user_card = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'email', 'user_card']


class ProfileSerializer(serializers.ModelSerializer):

    # user_cards = CardSerializer(read_only=True)
    def create(self, validated_data):
        user = Profile(
            email=validated_data["email"],
            cpf=validated_data["cpf"],
            birth_date=validated_data['birth_date'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            status_user=validated_data['status_user'],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.status_user = validated_data.get('status_user', instance.status_user)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = ['id', 'cpf', 'first_name', 'last_name', 'birth_date', 'status_user', 'email', 'password']
        read_only_fields = ['date_joined', 'last_login', 'user_permissions', 'groups', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}