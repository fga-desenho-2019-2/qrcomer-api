from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from user_service.models import (
  Profile
)
from user_service.api.serializers import (
  UserSerializer,
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


@api_view(["GET", "POST", "DELETE", "PUT"])
def user(request, id):
  """
    List, create, update or delete a user
  """
  try:
    profile = Profile.objects.get(pk=id)
  except:
    return JsonResponse({"message": "Usuário não existe"}, status=404)

  if request.method == 'GET':
    serializer = UserSerializer(profile)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = UserSerializer(profile, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
  
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    # Validação dos dados
    try:
      exist_cpf = Profile.objects.get(cpf=data['cpf'])
    except:
      pass
    
    if (exist_cpf):
      return JsonResponse({"msg": "Este usuário já existe"}, status=404)
    return Response("Oi")
    # serializerUser = UserSerializer(data=data)
    # serializerProfile = ProfileSerializer(data=data)
    # if serializerUser.is_valid() and serializerProfile.is_valid():
      # return Response({"msg": "Ok"})
      # exist_cpf = Profile.objects.get(cpf=data['cpf'])
      # serializerUser.save()
    # return Response({"msg": "Falha"})
    
  elif request.method == 'DELETE':
    profile.delete()
    return HttpResponse(status=204)
