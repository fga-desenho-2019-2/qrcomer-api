from rest_framework.response import Response
from rest_framework import status
from ..models import Profile
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import authentication


class SessionView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication,
                              authentication.BasicAuthentication,)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairPatchedSerializer

    token_obtain_pair = TokenObtainPairView.as_view()
    

class CreateUserProfile(SessionView):

    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
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
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    # @api_view(["PATCH"])
    # def patch_user(request, cpf):
    #     profile = Profile.objects.filter(cpf=cpf)
    #     if not profile:
    #         return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
    #     return Response("Nada")
    #
    # @api_view(["DELETE"])
    # def delete_user(request, cpf):
    #     profile = Profile.objects.filter(cpf=cpf)
    #     if not profile:
    #         return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
    #     return Response("Nada")