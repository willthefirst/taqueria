from django.test import TestCase, Client
from django.urls import reverse
from guacamole.posts.models import Post
from urllib.parse import urlencode
from django.conf import settings
import os

class GlobalViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_404_page(self):
        response = self.client.get('/asdf')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        
class RegistrationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_registration/registration_form.html')
        
    def test_registration_complete_page(self):
        response = self.client.get('/accounts/register/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_registration/registration_complete.html')
        
    def test_activation_page(self):
        response = self.client.get('/accounts/activate/?activation_key=123456789')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_registration/activation_form.html')

    def test_activation_complete_page(self):
        response = self.client.get('/accounts/activate/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_registration/activation_complete.html')

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        # Assert that this is using the custom login page located at guacamole/templates/registration/logged_out.html, not the default one from django admin
        expected_template_path = os.path.join(settings.BASE_DIR, 'guacamole', 'templates', 'registration', 'login.html')
        self.assertEqual(response.templates[0].origin.name, expected_template_path)
    
    def test_logged_out_page(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)
        print(response.templates[0].origin)
        self.assertTemplateUsed(response, 'registration/logged_out.html')
        # Assert that this is using the custom logout page located at guacamole/templates/registration/logged_out.html, not the default one from django admin
        expected_template_path = os.path.join(settings.BASE_DIR, 'guacamole', 'templates', 'registration', 'logged_out.html')
        self.assertEqual(response.templates[0].origin.name, expected_template_path)

    def test_password_reset_page(self):
        response = self.client.get('/accounts/password_reset/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')

    def test_password_reset_done_page(self):
        response = self.client.get('/accounts/password_reset/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_done.html')

    def test_password_reset_confirm_page(self):
        # Assuming 'uidb64' and 'token' are placeholders for actual values
        response = self.client.get('/accounts/reset/uidb64/token/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_confirm.html')

    def test_password_reset_complete_page(self):
        response = self.client.get('/accounts/reset/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_complete.html')
 