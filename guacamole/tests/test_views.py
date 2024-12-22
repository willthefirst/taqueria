from django.test import TestCase, Client
from django.urls import reverse
from guacamole.models import Post

class GlobalViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_404_page(self):
        response = self.client.get('/asdf')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

class PostsViewTestCase(TestCase):
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