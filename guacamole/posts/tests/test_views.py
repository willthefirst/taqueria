
from django.test import TestCase, Client
from django.urls import reverse
from guacamole.posts.models import Post
from urllib.parse import urlencode
from django.contrib.auth.models import User

"""
Authorization
"""
# No post routes should be accessible without authentication
class AuthTestCase(TestCase):
  def setUp(self):
    self.client = Client()
  
  def test_unauthorized_user(self):
    response = self.client.get('/posts/')
    self.assertEqual(response.status_code, 401)
    
    response = self.client.get('/posts/?abc')
    self.assertEqual(response.status_code, 401)
    
    response = self.client.get('/posts/abc')
    self.assertEqual(response.status_code, 401)

  # A user should be able to edit and delete their own posts, but not other users' posts
  def test_unauthorized_user_post(self):
    user1 = User.objects.create_user(username='user1', password='password')
    user2 = User.objects.create_user(username='user2', password='password')
    post = Post.objects.create(age_group="18-24", state="CA", user=user1)
    
    self.client.login(username='user2', password='password')
    response = self.client.get(f'/posts/{post.id}/edit')
    self.assertEqual(response.status_code, 403)
    
    response = self.client.put(f'/posts/{post.id}', {'age_group': '25-64', 'state': 'NY'})
    self.assertEqual(response.status_code, 403)
    
    response = self.client.delete(f'/posts/{post.id}')
    self.assertEqual(response.status_code, 403)
    
    self.client.login(username='user1', password='password')
    response = self.client.get(f'/posts/{post.id}/edit')
    self.assertEqual(response.status_code, 200)
    
    form_data = {
        'age_group': '25-64',
        'state': 'NY'
    }
    
    response = self.client.put(
        f'/posts/{post.id}',
        data=urlencode(form_data),
        content_type='application/x-www-form-urlencoded'
    )
    
    response = self.client.delete(f'/posts/{post.id}')
    self.assertEqual(response.status_code, 200)
        
""" 
CRUD operations
"""
class CRUDTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        Post.objects.create(age_group="18-24", state="CA", user=self.user)
        
    def test_posts_list_page(self):
        url = reverse('api-1.0.0:get_posts') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/posts_list.html')

    def test_post_detail_page(self):
        url = reverse('api-1.0.0:get_post', args=[1]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_details.html')

    def test_post_detail_page_404(self):
        url = reverse('api-1.0.0:get_post', args=[99]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
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
        self.assertTemplateUsed(response, 'posts/post_creator.html')
    
    def test_get_post_editor(self):
        url = reverse('api-1.0.0:get_post_editor', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_editor.html')
    
    def test_delete_post(self):
        url = reverse('api-1.0.0:delete_post', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), 0)
