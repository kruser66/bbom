from blog.models import User
from django.test import TestCase


class LogInTest(TestCase):
    
    def setUp(self):
        self.credentials = {
            'email': 'kruser@yandex.ru',
            'name': 'Сергей',
            'password': 'admin'
        }
        User.objects.create_user(**self.credentials)
    
    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)