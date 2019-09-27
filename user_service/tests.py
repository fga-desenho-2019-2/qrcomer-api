from django.test import TestCase

# Create your tests here.
class UselessTest(TestCase):
    def setUp(self):
        print('Yay')

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(True, False)