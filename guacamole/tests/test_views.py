from django.test import TestCase, Client
from django.urls import reverse
from guacamole.models import Post
from urllib.parse import urlencode

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

class PostViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Post.objects.create(age_group="18-24", state="CA")
        
    def test_posts_list_page(self):
        url = reverse('api-1.0.0:get_posts') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts_list.html')

    def test_post_detail_page(self):
        url = reverse('api-1.0.0:get_post', args=[1]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_details.html')

    def test_post_detail_page_404(self):
        url = reverse('api-1.0.0:get_post', args=[99]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        
    def test_create_post(self):
        url = reverse('api-1.0.0:create_post')
        response = self.client.post(url, {'age_group': '25-64', 'state': 'NY'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 2)
        post = Post.objects.last()
        self.assertEqual(post.age_group, '25-64')
        self.assertEqual(post.state, 'NY')
    
    def test_update_post(self):
        url = reverse('api-1.0.0:update_post', args=[1])
        form_data = {
            'age_group': '25-64',
            'state': 'NY'
        }
        response = self.client.put(
            url,
            data=urlencode(form_data),
            content_type='application/x-www-form-urlencoded'
        )
        
        self.assertEqual(response.status_code, 200)
        post = Post.objects.get(id=1)
        self.assertEqual(post.age_group, '25-64')
        self.assertEqual(post.state, 'NY')
    
    def test_get_post_creator(self):
        url = reverse('api-1.0.0:get_post_creator')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_creator.html')
    
    def test_get_post_editor(self):
        url = reverse('api-1.0.0:get_post_editor', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_editor.html')
    
    def test_delete_post(self):
        url = reverse('api-1.0.0:delete_post', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), 0)