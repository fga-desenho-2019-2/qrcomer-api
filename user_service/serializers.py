from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    # def create(self, validated_data):
    #     client = Client.objects.create(
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #         cpf=validated_data['cpf'],
    #     )

    #     return client

class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"