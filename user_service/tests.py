from django.test import TestCase
from model_mommy import mommy
from .models import User

class TestUser(TestCase):
    def setUp(self):
        self.user = mommy.make(User,
            first_name = 'blanco',
            last_name = 'matheus',
            email = 'msallesblanco@gmail.com',
            cpf = '065.822.021-70'
        )
        
    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEquals(self.user.__str__(), self.user.first_name + self.user.last_name)