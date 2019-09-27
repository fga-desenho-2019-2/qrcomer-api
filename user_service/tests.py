from django.test import TestCase

# Create your tests here.
class UselessTest(TestCase):
    def setUp(self):
        print('Yay')

    def test_if_true_still_true(self):
        self.assertEqual(True, True)