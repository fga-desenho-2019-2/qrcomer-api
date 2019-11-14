from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from ..models import Profile, Card
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import authentication, generics
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)


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
        profile = Profile.objects.filter(status_user=True)
        if not profile:
            return Response({"message": "User not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCard(BaseView):

    serializer_class = CardSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Ajustar mensagem de retorno
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CardView(BaseView):

    """
    UserCardGetData, classe com os metodos GET(), UPDATE(), DELETE() para o cartão

    """
    serializer_class = CardSerializer

    lookup_field = 'number'

    def get_lookup_field(self):
        return self.lookup_field

    def delete(self, request, number):
        card = Card.objects.filter(number = number)
        if not card:
            return JsonResponse({"message": "No card found"}, status=HTTP_404_NOT_FOUND)
        card.delete()
        return JsonResponse({ "message": "Card deleted" }, status=HTTP_200_OK)


    def get(self, request, id):
        card = get_object_or_404(Card, id=id)
        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        card = get_object_or_404(Card, id=id)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileCards(generics.ListAPIView, BaseView):

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):

        profile_cpf = self.request.query_params.get('cpf', None)

        query_cards_list = Card.objects.filter(profile__cpf=profile_cpf) \
            .values('profile__email', 'profile__cpf', 'number')
        # print(query_cards_list)
        data = []

        cards = [item['number'] for item in query_cards_list]

        [data.append({
            'profile': {
                'email': item['profile__email'],
                'cpf': item['profile__cpf'],
            },
            'cards': cards}) for item in query_cards_list]

        for item in range(0, len(data)-1):
            data.pop()

        return Response({'data': data, 'title': 'Cartões do usuário'}, status=status.HTTP_200_OK)
