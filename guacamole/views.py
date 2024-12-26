from ninja import NinjaAPI
from ninja.security import django_auth
from .posts.views import router as posts_router

http = NinjaAPI(csrf=True)
http.add_router("/posts/", posts_router, auth=django_auth)