from django.http import HttpResponse
from django.template import loader
from ninja import NinjaAPI
from .models import Post
from ninja import Schema
from django.http import QueryDict
from .forms import RegistrationForm

http = NinjaAPI()

@http.get("/accounts/register/")
def sign_up(request):
  form = RegistrationForm()
  template = loader.get_template('registration/register.html')
  context = {
    'form': form
  }
  return HttpResponse(template.render(context, request))


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

@http.get("/posts/new")
def get_post_creator(request):
  template = loader.get_template('post_creator.html')
  return HttpResponse(template.render({}, request))

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

@http.get("/posts/{id}/edit")
def get_post_editor(request, id: int):
  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)
  
  template = loader.get_template('post_editor.html')
  context = {
    'post': post,
  }
  return HttpResponse(template.render(context, request))
    
@http.put("/posts/{id}")
def update_post(request, id: int):
  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)
  
  put = QueryDict(request.body)
  post.state = put.get('state')
  post.age_group = put.get('age_group')
  
  post.save()
  return HttpResponse(f'Post {post.id} updated', status=200)

@http.delete("/posts/{id}")
def delete_post(request, id: int):
  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)
  
  post.delete()
  return HttpResponse(f'Post {id} deleted', status=200)