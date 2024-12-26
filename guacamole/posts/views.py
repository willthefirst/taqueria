from django.http import HttpResponse, QueryDict
from django.template import loader
from ninja import Router
from .models import Post

router = Router()

@router.get("/")
def get_posts(request):
  posts = Post.objects.all().values()
  template = loader.get_template('posts_list.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))

@router.post("/")
def create_post(request):
  age_group = request.POST.get('age_group')
  state = request.POST.get('state')
  post = Post.objects.create(age_group=age_group, state=state)
  return HttpResponse(f'Post {post.id} created', status=201)

@router.get("/new")
def get_post_creator(request):
  template = loader.get_template('post_creator.html')
  return HttpResponse(template.render({}, request))

@router.get("/{id}")
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

@router.get("/{id}/edit")
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
    
@router.put("/{id}")
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

@router.delete("/{id}")
def delete_post(request, id: int):
  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)
  
  post.delete()
  return HttpResponse(f'Post {id} deleted', status=200)