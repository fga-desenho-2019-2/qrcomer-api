from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from ..models import Profile, Card
from .serializers import ProfileSerializer, CardSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication, generics


class SessionView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication,
                              authentication.BasicAuthentication,)


class CreateUserProfile(SessionView):
    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Ajustar mensagem de retorno
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)


class UserProfileView(SessionView):
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = Profile.objects.filter(status_user=True)
        if not profile:
            return Response({"message": "User not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCardCreate(SessionView):
    serializer_class = CardSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Ajustar mensagem de retorno
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserCardGetData(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    lookup_field = 'number'

    def get(self, request, id):
        card = get_object_or_404(Card, id=id)
        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileCards(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):

        profile_id = self.request.query_params.get('id', None)

        query_cards_list = Card.objects.filter(profile_id__in=profile_id) \
            .values('profile__email', 'number')

        data = []

        cards = [item['number'] for item in query_cards_list]

        [data.append({
            'profile': item['profile__email'],
            'cards': cards})
            for item in query_cards_list]

        for item in range(0, len(data)-1):
            data.pop()

        return Response({'data': data, 'title': 'Cartões do usuário'}, status=status.HTTP_200_OK)
