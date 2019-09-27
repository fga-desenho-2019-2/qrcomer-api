from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .serializers import RegistrationUser
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def registration_user(request):
    serializer = RegistrationUser(data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'Usuário registrado com sucesso'
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['email'] = user.email
        data['cpf'] = user.cpf

    else:
        data = serializer.errors

    return Response(data)