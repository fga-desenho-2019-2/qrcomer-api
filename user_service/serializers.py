from .models import User
from rest_framework import serializers

class RegistrationUser(serializers.ModelSerializer):

    # conf_password = serializers.CharField(
    #     style = { 'input_type': 'password' },
    #     write_only = True
    # )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'cpf']

    def save(self):
        user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'],
            cpf = self.validated_data['cpf']
        )

        # password = self.validated_data['password']
        # conf_password = self.validated_data['password2']

        # if len(password) < 8:
        #     raise serializers.ValidationError(
        #         { 'password': 'A senha precisa ter no mínimo 8 caracteres' }
        #     )

        # if password != conf_password:
        #     raise serializers.ValidationError(
        #         { 'password': 'As senhas precisam ser iguais' }
        #     )

        # user.set_password(password)
        user.save()

        return user