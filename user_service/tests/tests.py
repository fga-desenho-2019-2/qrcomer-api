from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Profile, Card
from django.urls import reverse
from .factory import UserFactory, CardFactory
from django.core import serializers
import factory

class TestProfileUser(APITestCase):
    

    def setUp(self):
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        self.url_create = reverse('post_user')
        self.url_edit = reverse('edit_user', kwargs={'cpf': self.user_data['cpf']})
        self.url_get = reverse('get_user', kwargs={'cpf': self.user_data['cpf']})

    def test_create_profile(self):
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_with_wrong_cpf_number_values(self):
        self.user_data['cpf'] = '68532168532'
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_profile_with_wrong_cpf_format(self):
        self.user_data['cpf'] = '653210'
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_with_wrong_password(self):
        self.user_data['password'] = '123'
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_without_first_name(self):
        self.user_data['first_name'] = ''
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_without_last_name(self):
        self.user_data['last_name'] = ''
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_create_profile_with_wrong_birth_date_format(self):
        self.user_data['birth_date'] = '15-11-1996'
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile_with_birth_date_less_than_eighteen(self):
        self.user_data['birth_date'] = '2005-08-20'
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_edit_profile(self):
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

        self.user_data['first_name'] = 'Novo nome'

        response_edit = self.client.put(self.url_edit, self.user_data, format='json')
        self.assertEqual(response_edit.status_code, status.HTTP_200_OK)

    def test_edit_profile_bad_request(self):
        response = self.client.post(self.url_create, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

        self.user_data['cpf'] = '123'

        response_edit = self.client.put(self.url_edit, self.user_data, format='json')
        self.assertEqual(response_edit.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_profile(self):
        self.client.post(self.url_create, self.user_data, format='json')
        response = self.client.get(self.url_get, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cpf'], self.user_data['cpf'])
    
    def test_get_profile_list(self):
        self.client.post(self.url_create, self.user_data, format='json')
        response = self.client.get(reverse('list_user'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_list_404(self):
        response = self.client.get(reverse('list_user'), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

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
        response = self.client.post(self.url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_card_wrong_holder_name_format(self):
        self.card_data['holder_name'] = 'te'
        response = self.client.post(self.url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)