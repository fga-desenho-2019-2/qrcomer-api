from rest_framework.serializers import ModelSerializer
from user_service.models import Profile

class UserSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
