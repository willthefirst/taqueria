from django.http import HttpResponse
from django.template import loader
from .models import Post

def get_posts(request):
  posts = Post.objects.all().values()
  template = loader.get_template('posts_list.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))

def get_post(request, id):
  post = Post.objects.get(id=id)
  template = loader.get_template('post_details.html')
  context = {
    'post': post,
  }
  return HttpResponse(template.render(context, request))