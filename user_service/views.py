from .models import Client
from django.http import HttpResponse, JsonResponse
from .serializers import ClientSerializer
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

@api_view(['POST'])
def register_client(request):
    serializer = ClientSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        client = serializer.save()
        data['response'] = 'Usuário registrado com sucesso'

    else:
        data = serializer.errors

    return Response(data)

@api_view(['DELETE'])
def delete_client(request, registro):
    try:
        client = Client.objects.get(pk=registro)
    except Client.DoesNotExist:
        return HttpResponse(status=404)
    client.delete()
    return HttpResponse(status=204)

@api_view(["POST"])
def list_clients(request):
    clients = Client.objects.all().values()
    return Response(data=clients)

# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = User.objects.filter(cpf=serializer.data["cpf"]).first()
#         if(user):
#             user = UserSerializer.create(serializer, request.data)
#             return Response({"Usuário cadastrado com sucesso!"})
#     else:
#         return Response({"Dados incorretos! Tente novamente"})
