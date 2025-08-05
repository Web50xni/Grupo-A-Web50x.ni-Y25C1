from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # El modelo User, heredará los campos de la clase AbstractUser, tales como first_name, last_name, username, password, etc.
    # Si no se desea agregar otro campo adicional, se omite con la palabra reservada 'pass'
    pass

# Modelo Tarea

# Una tarea puede permanecer en uno de tres estados: Pendiente(inicial), En proceso, Completada, Rechazada
# El atributo choices recibe una lista de tuplas. El primer elemento corresponde a cómo se guarda en la base de datos, el segundo, cómo se muestra en la Interfaz.
estadosTarea = [
    ('pending', 'Pendiente'),
    ('process', 'En proceso'),
    ('Fulfilled', 'Completada'),
    ('Rejected', 'Rechazada')
]

class Tarea(models.Model):
    contenido = models.TextField(max_length=200, blank=False, null=False)
    estado = models.CharField(default=estadosTarea[0][0], choices=estadosTarea, blank=False, null=False) # El valor por defecto/incial de una tarea será 'pending'
    fechaCreacion = models.DateTimeField(auto_now_add=True) # Asigna automáticamente la fecha y hora actual según se configure en settings.py
    # Vincular cada tarea a un Usuario
    #creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="TareaUser") # models.CASCADE: Cuando el registro de un usuario se elimina, los objetos relacionados también. (Tareas)