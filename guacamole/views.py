from ninja import NinjaAPI
from ninja.security import django_auth
from .posts.views import router as posts_router
from .accounts.views import router as accounts_router

http = NinjaAPI(csrf=True)
http.add_router("/accounts/", accounts_router, auth=django_auth)
http.add_router("/posts/", posts_router, auth=django_auth)