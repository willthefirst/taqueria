from django.urls import path, include
from .views import http
  
urlpatterns = [
  path("accounts/", include("django.contrib.auth.urls")),
  path("", http.urls),
]