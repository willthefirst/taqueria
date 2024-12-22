from django.urls import path
from .views import http
  
urlpatterns = [
  path("", http.urls),
]