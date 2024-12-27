from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def test_user_created_signal(self):
        user = User.objects.create_user(username='test', password='test')
        self.assertTrue(user.groups.filter(name='Posts').exists())
        