from django.urls import path
from .views import HomeView, ContactFormView, SupportFormView, GraciasView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('contacto/', ContactFormView.as_view(), name='contacto'),
    path('soporte/', SupportFormView.as_view(), name='soporte'),
    path('gracias/', GraciasView.as_view(), name='gracias'),
]