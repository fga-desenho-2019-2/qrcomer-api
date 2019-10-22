from rest_framework import serializers
from ..models import Profile
import datetime
# from dateutil.relativedelta import relativedelta
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Profile(
            email=validated_data["email"],
            cpf=validated_data["cpf"],
            birth_date=validated_data['birth_date'],
            sex=validated_data['sex'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
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

    # Validators 

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("Invalid CPF size!")
        else:
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
            if second_digit_validator == '10':
                second_digit_validator = '0'

            if first_digit_validator == value[-2] and second_digit_validator == value[-1]:
                return value
            else:
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
