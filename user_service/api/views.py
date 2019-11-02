from rest_framework.response import Response
from rest_framework import status
from ..models import Profile
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import authentication


class BaseView(APIView):
    """
    BaseView, responsável pelas classes de autenticação e por definir o
    serializer_class
    """
    serializer_class = ProfileSerializer

    authentication_classes = (
        JSONWebTokenAuthentication, 
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
    )

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairPatchedSerializer

    token_obtain_pair = TokenObtainPairView.as_view()
    

class CreateUserProfile(BaseView):
    """
    CreateUserProfile, responsável por criar o usuário
    rota: user/ (POST)
    """
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserProfile(BaseView):
    """
    EditUserProfile, responsável por editar o usuário
    rota: user/<CPF> (PUT)
    """
    def put(self, request, cpf, format=None):
        profile = get_object_or_404(Profile, cpf=cpf)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(BaseView):
    """
    UserProfile, responsável por listar um usuário dado seu cpf
    rota: user/<CPF> (GET)
    """
    def get(self, request, cpf):
        profile = get_object_or_404(Profile, cpf=cpf)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileView(BaseView):
    """
    UserProfileView, responsável por listar todos os usuários
    rota: user/(GET)
    TODO: Paginação e permitir que somente um admin tenha acesso ao método
    """
    def get(self, request):
        profile = Profile.objects.all()
        if not profile:
            return Response({"message": "User not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)


    # @api_view(["PATCH"])
    # def patch_user(request, cpf):
        