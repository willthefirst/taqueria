from django.urls import path
from .views import api
  
urlpatterns = [
  path("api/", api.urls),
]