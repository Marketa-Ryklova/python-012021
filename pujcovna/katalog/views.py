from django.http import HttpResponse
from django.views import View

class IndexView(View):
  def get(self, request):
    return HttpResponse('Zde bude titulní stránka.')