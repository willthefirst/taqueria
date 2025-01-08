from django.test import TestCase, Client
from django.contrib.auth.models import User

class AccountViewsTestCase(TestCase):
    def test_user_can_remove_account(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.delete('/accounts/')
        self.assertEqual(User.objects.count(), 0)
        # After successful deletion, user is redirected to the login page
        self.assertEqual(response.status_code, 302)
        # Check that it sets the location header to '/accounts/deletion/complete'
        # print(response)
        # self.assertEqual(response['Location'], '/accounts/deletion/complete')
