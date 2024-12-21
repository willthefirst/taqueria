from django.test import TestCase, Client
from django.urls import reverse
from guacamole.models import Post

class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Post.objects.create(age_group="18-24", state="CA")
        
    def test_posts_list_page(self):
        url = reverse('posts_list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts_list.html')

    def test_post_detail_page(self):
        url = reverse('post_detail', args=[1]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_details.html')
    
    def test_post_detail_page_404(self):
        url = reverse('post_detail', args=[99]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')