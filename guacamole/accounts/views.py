from django.http import HttpResponseRedirect
from django.urls import reverse
from ninja import Router

router = Router()

@router.delete("/")
def delete_account(request):
  request.user.delete()
  request.session.flush()
  return HttpResponseRedirect(reverse('api-1.0.0:account_deleted'), status=303)

@router.get("/logout")
def log_out(request):
  request.session.flush()
  return HttpResponseRedirect(reverse('api-1.0.0:logged_out'), status=303)
