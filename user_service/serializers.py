from .models import User
from rest_framework import serializers

class RegistrationUser(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, label="Endereco Email")
    password = serializers.CharField(required=True, label="Senha", style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance