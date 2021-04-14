from django.urls import path

from . import views

urlpatterns = [
  path('', views.SeznamView.as_view(), name='index'),
]