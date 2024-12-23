from django.urls import path, include
from .views import http
  
urlpatterns = [
  path("accounts/", include("django_registration.backends.activation.urls")),
  path("accounts/", include("django.contrib.auth.urls")),
  path("", http.urls),
]