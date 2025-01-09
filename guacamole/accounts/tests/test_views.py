from django.test import TestCase, Client
from django.contrib.auth.models import User

class AccountViewsTestCase(TestCase):
    def test_user_can_remove_account(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.delete('/accounts/')
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 303)
        self.assertEqual(response['Location'], '/account-deleted')
