from user_service.models import Client
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .serializers import ClientSerializer
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

    queryset = Client.objects.all()
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer

@api_view(['POST'])
def register_client(request):
    serializer = ClientSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        order = serializer.save()
        data['response'] = 'Usuário registrado com sucesso'

    else:
        data = serializer.errors

    return Response(data)

@api_view(["POST"])
def list_clients(request):
    clients = Client.objects.all().values()
    return Response(data=clients)

@api_view(['DELETE'])
def delete_client(request, registro):

    # If request is valid
    client = Client.objects.get(pk=registro)
    if (registro == None):
        return Response({'error': 'Formulário inválido.'},
                                status=HTTP_400_BAD_REQUEST)
    # If order exist
    try:
        client = Client.objects.get(pk=registro)
    except:
        return Response({'error': 'Produto não existe.'},
                                status=HTTP_404_NOT_FOUND)
    client.delete()
    return HttpResponse(status=204)


@api_view(["POST"])
def edit_client(request, registro):
    client = Client.objects.get(pk=registro)
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')


    if(registro == None):
        return Response({'error':'Falha na requisição.'},status=HTTP_400_BAD_REQUEST)

    try:
        client = Client.objects.get(pk=registro)
    except:
        return Response({'error': 'Cliente não existe.'},
                                status=HTTP_404_NOT_FOUND)
    serializer = ClientSerializer(client, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
