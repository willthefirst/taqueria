from django.http import HttpResponse
from django.template import loader
from .models import Post

def get_posts(request):
  posts = Post.objects.all().values()
  template = loader.get_template('post_list.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))