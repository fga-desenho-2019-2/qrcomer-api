from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile
from django.urls import reverse


class ProfileUserTest(APITestCase):
    url = reverse('post_user')

    def test_create_profile(self):

        data = {
                'cpf': '06066875132',
                'first_name': 'Leonardo',
                'last_name': 'barreiros',
                'birth_date': '1996-11-14',
                'sex': 'm',
                'email': 'leossb@teste.com',
                'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_with_wrong_cpf_number_values(self):
        data = {
            'cpf': '68532168532',
            'first_name': 'Leonardo',
            'last_name': 'barreiros',
            'birth_date': '1996-11-14',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_profile_with_wrong_cpf_format(self):
        data = {
            'cpf': '653210',
            'first_name': 'Leonardo',
            'last_name': 'barreiros',
            'birth_date': '1996-11-14',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_with_wrong_password(self):
        data = {
            'cpf': '06066875132',
            'first_name': 'Leonardo',
            'last_name': 'barreiros',
            'birth_date': '1996-11-14',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'asd'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_without_first_name(self):
        data = {
            'cpf': '06066875132',
            'first_name': '',
            'last_name': 'barreiros',
            'birth_date': '1996-11-14',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_without_last_name(self):
        data = {
            'cpf': '06066875132',
            'first_name': 'Leonardo',
            'last_name': '',
            'birth_date': '1996-11-14',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_with_wrong_birth_date_format(self):
        data = {
            'cpf': '06066875132',
            'first_name': 'Leonardo',
            'last_name': '',
            'birth_date': '15-11-1996',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_with_birth_date_less_than_eighteen(self):
        data = {
            'cpf': '06066875132',
            'first_name': 'Leonardo',
            'last_name': '',
            'birth_date': '2005-08-20',
            'sex': 'm',
            'email': 'leossb@teste.com',
            'password': 'teste@!'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
