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

@http.post("/posts/")
def create_post(request):
    age_group = request.POST.get('age_group')
    state = request.POST.get('state')
    post = Post.objects.create(age_group=age_group, state=state)
    return HttpResponse(f'Post {post.id} created', status=201)

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

 
