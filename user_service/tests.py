# from django.test import TestCase
# from .models import Client
# from rest_framework.test import APITestCase
# import json
# from django.core import serializers
# from .serializers import ClientSerializer

# class CheckCLientAPITest(APITestCase):

#     def test_register_client_with_correct_params(self):
#         # If user was successfully created
#         request_1 = {'registro':'123', 'first_name':'Matheus', 'last_name':'Blanco', 'email':'msallesblanco2gmail.com', 'password':'12345678', 'cpf':'065.822.021-70'}
#         response_1 = self.client.post('/register_client/', request_1)
#         self.assertEqual(response_1.status_code, 200)

#     def test_register_client_with_status_0(registro, status=0):

#         registro = 1
#         first_name = 'xiu'
#         last_name = 'xau'
#         email = 'xiuxau@gmail.com'
#         password = '12345698'
#         cpf = '065.922.021-70'


#         Client.objects.create(
#             registro = registro,
#             first_name = first_name,
#             last_name = last_name,
#             email = email,
#             password = password,
#             cpf = cpf
#         )

#     def test_delete_client_with_wrong_id(self):
#         request_1 = {'registro':'123', 'first_name':'Matheus', 'last_name':'Blanco', 'email':'msallesblanco2gmail.com', 'password':'12345678', 'cpf':'065.822.021-70'}
#         self.client.post('/delete_client/', request_1)

#         # INTERNAL REQUEST ERROR if order does not exist
#         request_2 = {'registro': 'p'}
#         response_2 = self.client.post('/delete_client/', request_2)
#         self.assertEqual(response_2.status_code, 404)

#     def test_list_clients(self):
#         request_1 = {}
#         response_1 = self.client.post('/list_clients/', request_1)
#         self.assertEqual(response_1.status_code, 200)

#     def test_edit_client_with_missing_params(self):
#         request_1 = {'registro':'123', 'first_name':'Matheus', 'last_name':'Blanco', 'email':'msallesblanco2gmail.com', 'password':'12345678', 'cpf':'065.822.021-70'}
#         response_1 = self.client.post('/register_client/', request_1)
#         response_1 = self.client.post('edit_client/', request_1)
#         self.assertEqual(response_1.status_code, 404)
