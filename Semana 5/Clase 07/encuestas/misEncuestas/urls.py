from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('encuestas/<str:tema>/', views.encuesta, name="encuestas")
]