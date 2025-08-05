
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoApp.urls')) # Las rutas de la todoApp se referencian directamente a la ruta principal.
]
