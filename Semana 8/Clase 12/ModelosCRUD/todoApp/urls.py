from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('editar/<int:ID>', views.editarTarea, name="editarTarea"),
    path('terminar/<int:ID>', views.terminarTarea, name="terminarTarea"),
    path('eliminar/<int:ID>', views.eliminarTarea, name="eliminarTarea")
]