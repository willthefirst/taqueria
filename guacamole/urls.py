from django.urls import path
from . import views

urlpatterns = [
  path('posts/', views.get_posts, name='TODO_YABADABA_REPLACE_ME'),
]

