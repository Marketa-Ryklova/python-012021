from django.http import HttpResponse
from django.views import View

class IndexView(View):
  def get(self, request):
    return HttpResponse('Zde bude titulní stránka'
                        '       '
                        '     '
                        
                        "<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>"
                        """<h1>Vítejte v nejlepší autopůjčovně!</h1>
                        <a href='http://localhost:8000/katalog/seznam/'>Auta, která nabízíme?</a><br>
                        <h2>O nás</h2>
                        <p>Naše půjčovna vznikla v roce 2021 a dnes nabízí přibližně 30 aut. Především značky Škoda, Peugeot, VW.</p>
                        """
                        )



class SeznamView(View):
  def get(self, request):
   return HttpResponse('Zde bude seznam aut.')