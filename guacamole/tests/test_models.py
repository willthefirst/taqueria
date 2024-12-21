from django.test import TestCase
from guacamole.models import Post

class PostTestCase(TestCase):
    def setUp(self):
      Post.objects.create(state="CA")
    
    def test_(self):
      """Can read a post"""
      post = Post.objects.get(state="CA")
      self.assertEqual(post.state, "CA")