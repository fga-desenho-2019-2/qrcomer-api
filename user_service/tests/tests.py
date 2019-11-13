from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Profile, Card
from django.urls import reverse
from .factory import UserFactory, CardFactory
from django.core import serializers
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
    


class test_request_card(APITestCase):

    url = reverse('post_card')

    def setUp(self):
        self.card_data = factory.build(dict, FACTORY_CLASS=CardFactory)
        self.user_data = UserFactory()
        self.card_data['profile'] = self.user_data.id
    
    def test_create_card(self):
        response = self.client.post(self.url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 1)

    def test_create_card_with_wrong_number_format(self):
        self.card_data['number'] = '123456789'
        response = self.client.post(self.url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_card_wrong_cvv_format(self):
        self.card_data['cvv'] = "12"
        print(self.card_data)
        response = self.client.post(self.url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_card_wrong_holder_name_format(self):
        self.card_data['holder_name'] = 'te'
        response = self.client.post(self.url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)