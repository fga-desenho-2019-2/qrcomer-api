from rest_framework import serializers
from user_service.models import Profile

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
