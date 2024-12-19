from django.urls import path
from . import views

urlpatterns = [
  path('posts/', views.get_posts, name='posts_list'),
  path('posts/<int:id>', views.get_post, name='post_detail'),
]

