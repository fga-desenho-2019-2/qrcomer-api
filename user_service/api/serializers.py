from rest_framework import serializers
from ..models import Profile, Card
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_extra_fields.fields import Base64ImageField


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

    def validate_cpf_cnpj(self, value):

        if len(value) != 11:
            raise serializers.ValidationError("Invalid CPF size!")

        sum = 0
        first_digit_validator = 0
        second_digit_validator = 0

        for i in range(9):
            sum += int(value[i])*(10-i)

        first_digit_validator = str((sum*10) % 11)

        sum = 0

        for i in range(10):
            sum += int(value[i])*(11-i)

        second_digit_validator = str((sum*10) % 11)

        if str(first_digit_validator)[-1] == value[-2] and str(second_digit_validator)[-1] == value[-1]:
            return value
        raise serializers.ValidationError("Invalid CPF digits!")

    def validate_number(self, value):
        if len(value) != 16:
            raise serializers.ValidationError("Error: Invalid Number Card format")
        return value

    def validate_cvv(self, value):
        if len(value) != 3:
            raise serializers.ValidationError('Error: Invalid CVV format')
        return value

    def validate_validation(self, value):
        # Check if card its not older
        if (datetime.date.today() - value) > datetime.timedelta(days=365*10):
            raise serializers.ValidationError("Error: Invalid Data Card format")
        return value

    def validate_holder_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError('Error: Invalid CVV format')
        return value

class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Extra data to Token response
        data['user_data'] = {
            'email': self.user.email,
            'cpf' :self.user.cpf
        }
        return data


class ProfileSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def create(self, validated_data):
        user = Profile(
            **validated_data
        )
        
        image = validated_data.pop('image')
        user.image = image
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = ['id', 'cpf', 'first_name', 'last_name', 'birth_date', 'status_user', 'email', 'password', 'image']
        read_only_fields = ['date_joined', 'last_login', 'user_permissions', 'groups', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    # Validators

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("Invalid CPF size!")

        sum = 0
        first_digit_validator = 0
        second_digit_validator = 0

        for i in range(9):
            sum += int(value[i])*(10-i)

        first_digit_validator = str((sum*10) % 11)

        sum = 0

        for i in range(10):
            sum += int(value[i])*(11-i)

        second_digit_validator = str((sum*10) % 11)

        if str(first_digit_validator)[-1] == value[-2] and str(second_digit_validator)[-1] == value[-1]:
            return value
        raise serializers.ValidationError("Invalid CPF digits!")
    
    def validate_birth_date(self, value): 
        # Check if user age >= 18
        if (datetime.date.today() - value) < datetime.timedelta(days=365*18):
            raise serializers.ValidationError("Invalid date!!")
        return value

    def validate_password(self, value):
        # Check the minimum size of password
        if len(value) < 4:
            raise serializers.ValidationError('Required 4 or more digits to password!')
        return value

class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    def update(self, user, validated_data):
        image = validated_data.pop('image')
        user.image = image
        user.save()
        return user

    class Meta:
        model = Profile
        fields = ['cpf', 'image']
