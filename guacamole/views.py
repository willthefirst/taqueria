from django.http import HttpResponse
from ninja import NinjaAPI
from ninja.security import django_auth
from .posts.views import router as posts_router
from .accounts.views import router as accounts_router
from django.template import loader

http = NinjaAPI(csrf=True)
http.add_router("/accounts/", accounts_router, auth=django_auth)
http.add_router("/posts/", posts_router, auth=django_auth)

@http.get("/account-deleted")
def account_deleted(request):
    template = loader.get_template('accounts/deletion_complete.html')
    return HttpResponse(template.render({}, request))

@http.get("/logged-out")
def logged_out(request):
    template = loader.get_template('registration/logged_out.html')
    return HttpResponse(template.render({}, request))