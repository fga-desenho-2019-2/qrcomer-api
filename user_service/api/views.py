from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from user_service.models import (
  Profile
)
from user_service.api.serializers import (
  ProfileSerializer
)

@api_view(["GET"])
def users(request):
  """
    List all users
  """
  users = Profile.objects.all()
  serializer = ProfileSerializer(users, many=True)
  return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_user(request, cpf):
  """
    List a user
  """
  profile = Profile.objects.filter(cpf=cpf)
  if not profile:
    return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
  serializer = ProfileSerializer(profile, many=True)
  data = serializer.data
  return Response(data, status=HTTP_200_OK)


@api_view(["POST"])
def post_user(request):
  data = JSONParser().parse(request)
  new_user = ProfileSerializer(data=data)
  if new_user.is_valid():
    new_user.save()
    # Ajustar para retornar token do usuário
    return Response(new_user.data, status=HTTP_201_CREATED)
  else:
    # Ajustar mensagem de retorno
    return Response({"message": "Can not create user"}, status=HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def patch_user(request, cpf):
  profile = Profile.objects.filter(cpf=cpf)
  if not profile:
    return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
  return Response("Nada")



@api_view(["DELETE"])
def delete_user(request, cpf):
  profile = Profile.objects.filter(cpf=cpf)
  if not profile:
    return JsonResponse({"message": "User not exists"}, status=HTTP_404_NOT_FOUND)
  return Response("Nada")