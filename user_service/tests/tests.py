from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Profile
from django.forms.models import model_to_dict
from django.urls import reverse
from .factory import UserFactory
import factory

class TestProfileUser(APITestCase):
    url = reverse('post_user')

    def setUp(self):
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)
    
    def test_create_profile(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_with_wrong_cpf_number_values(self):
        self.user_data['cpf'] = '68532168532'
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_profile_with_wrong_cpf_format(self):
        self.user_data['cpf'] = '653210'
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_with_wrong_password(self):
        self.user_data['password'] = '123'
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_without_first_name(self):
        self.user_data['first_name'] = ''
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_without_last_name(self):
        self.user_data['last_name'] = ''
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_with_wrong_birth_date_format(self):
        self.user_data['birth_date'] = '15-11-1996'
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_with_birth_date_less_than_eighteen(self):
        self.user_data['birth_date'] = '2005-08-20'
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
