from rest_framework.response import Response
from rest_framework import status
from ..models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class CreateUserProfile(CreateAPIView):

    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Ajustar mensagem de retorno
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):

    serializer_class = ProfileSerializer

    def get(self, request, cpf):
        profile = get_object_or_404(Profile, cpf=cpf)
        serializer = ProfileSerializer(profile)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)


class UserProfileView(APIView):

    serializer_class = ProfileSerializer

    def get(self, request):

        profile = Profile.objects.all()
        if not profile:
            return Response({"message": "User not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

#
#
#
#


    #
    # @api_view(["PATCH"])
    # def patch_user(request, cpf):
    #     profile = Profile.objects.filter(cpf=cpf)
    #     if not profile:
    #         return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
    #     return Response("Nada")
    #
    #
    #
    # @api_view(["DELETE"])
    # def delete_user(request, cpf):
    #     profile = Profile.objects.filter(cpf=cpf)
    #     if not profile:
    #         return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
    #     return Response("Nada")