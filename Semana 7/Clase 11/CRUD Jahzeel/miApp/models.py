from django.db import models

# Create your models here.

estados = [
    ('peding', 'Pendiente'),
    ('process', 'En Proceso'),
    ('fulfilled', 'Completada'),
    ('Rejected', 'Rechazada'),
]

class Tarea(models.Model):
    contenido = models.CharField(max_length=200)
    estado = models.CharField(max_length=100, default=estados[0][0], choices=estados)
    fecha = models.DateTimeField(auto_now_add=True)