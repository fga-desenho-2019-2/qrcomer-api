from rest_framework.response import Response
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


class UserProfile(SessionView):

    serializer_class = ProfileSerializer

    def get(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)


class UserProfileView(SessionView):

    serializer_class = ProfileSerializer

    def get(self, request):

        profile = Profile.objects.all()
        if not profile:
            return Response({"message": "User not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCardCreate(SessionView):

    serializer_class = CardSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Ajustar mensagem de retorno
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserCardGetData(SessionView):

    def get(self, request, id):
        card = get_object_or_404(Card, profile_id=id)
        serializer = CardSerializer(card)
        return Response({'Card': serializer.data}, status=status.HTTP_200_OK)


# class UserCardsUpdate(generics.UpdateAPIView):
#
#     serializer_class = CardSerializer
#
#     def put(self, request, id):
#         instance = get_object_or_404(Card, id=id)
#         context = {
#             'profile': instance.profile,
#             'number': instance.number,
#             'cvv': instance.cvv,
#             'validation': instance.validation,
#             'holder_name': instance.holder_name,
#             'cpf_cnpj': instance.cpf_cnpj
#         }
#         serializer = CardSerializer(data=context)
#         if serializer.is_valid():
#             self.perform_update(serializer)
#
#         return Response(serializer.data)