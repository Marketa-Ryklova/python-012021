
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('katalog/', include("katalog.urls")),
    path('seznam/', include("katalog.urls")),
]