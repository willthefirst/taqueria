from django.http import HttpResponse
from ninja import Router
from django.template import loader

router = Router()

@router.delete("/")
def delete_account(request):
  print('here')
  request.user.delete()
  # Load deletion_copmlete.html template
  template = loader.get_template('accounts/deletion_complete.html')
  return HttpResponse(template.render({}, request), status=302)