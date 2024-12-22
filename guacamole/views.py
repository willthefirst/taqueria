from django.http import HttpResponse
from django.template import loader
from ninja import NinjaAPI
from .models import Post

http = NinjaAPI()

@http.get("/posts/")
def get_posts(request):
  posts = Post.objects.all().values()
  template = loader.get_template('posts_list.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))

@http.get("/posts/{id}")
def get_post(request, id: int):
  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)
  
  template = loader.get_template('post_details.html')
  context = {
    'post': post,
  }
  return HttpResponse(template.render(context, request))

 
# TODO Going to have to sort this out AFTER setting up Django REST framework
# def create_post(request):
#   if request.method == 'POST':
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     post = Post.objects.create(title=title, content=content)
#     return HttpResponse(f'Post {post.id} created', status=201)
  
#   template = loader.get_template('create_post.html')
#   return HttpResponse(template.render({}, request))