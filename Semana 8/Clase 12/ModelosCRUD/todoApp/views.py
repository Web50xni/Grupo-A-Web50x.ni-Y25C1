from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import User, Tarea, estadosTarea
from django.shortcuts import get_object_or_404
from django.db.models import Q

"""
Algunos métodos para realizar consultas a los modelos:
    Modelo.objects.all(): Retorna todos los registros del Modelo.
    .get(id=n, cedula='cedula'): Retorna un solo registro que cumpla con los valores de campo indicadas en argumento. Si el registro no existe, provoca una excepción. (DoesNotExists)
    .filter(username='nombre', edad=n): Retorna los registros cuyos campos coincidan con los que se indiquen en argumentos. Si no se retorna ningún registro, no provoca excepción.
    usuario.delete() | registrosFiltrados.delete(): Permite eliminar el registro o registros a los que se concatene el método.
    registros.first(): Retorna/Selecciona el primer elemento que retornó la consulta al modelo (el primer objeto encontrado)
"""

# Create your views here.
def index(request):

    # Obtener los registros almacenados en las tablas, para retornarlos mediante método HTTP GET. A excepción de las tareas 'eliminadas'
    registrosTareas = Tarea.objects.exclude(Q(estado=estadosTarea[3][0]) | Q(estado=estadosTarea[2][0])) # Pueden pensar un <queryset[]> como un arreglo de objetos, pero más sencillo de manipular. Se retorna con cada consulta a un Modelo

    if request.method == 'POST':
        # Crear nueva tarea
        if 'nuevaTarea' in request.POST:
            #  Recibir los datos
            contenidoTarea = request.POST.get('contenido') # Equivalente a request.POST['contenido']

            if len(contenidoTarea) > 0:
                # Registrar la tarea en el modelo Tarea
                nuevaTarea = Tarea.objects.create(contenido=contenidoTarea)
                nuevaTarea.save() # Guardar registro

                # Regirigir al usuario (actualizar página)
                return HttpResponseRedirect(reverse('index'))

            # Entrada no válida:
            return render(request, 'todoApp/index.html', {
                'tareas': registrosTareas,
                'mensaje': 'No se puede registrar esta tarea.'
            })

    print(registrosTareas)
    

    return render(request, 'todoApp/index.html', {
        'tareas': registrosTareas
    })


def editarTarea(request, ID):
    # GET
    # Obtener el elemento a modificar utilizando su ID
    registro = get_object_or_404(Tarea, id=ID)

    # Modificar el estado del registro (si existe)
    registro.estado = estadosTarea[1][0]
    registro.save()


    return HttpResponseRedirect(reverse('index'))

def eliminarTarea(request, ID):
    # GET
    # Obtener el elemento a modificar utilizando su ID
    registro = get_object_or_404(Tarea, id=ID)

    # Modificar el estado del registro (si existe) [En este caso, no se borra el registro para mantener seguimiento. (En producción, rara vez se eliminan los datos de forma permanente)]
    registro.estado = estadosTarea[3][0] # Si realmente se requiere eliminar el registro (CRUD completo), se utiliza: registro.delete(), sin necesidad de guardar
    registro.save()


    return HttpResponseRedirect(reverse('index'))


def terminarTarea(request, ID):

    registro = get_object_or_404(Tarea, id=ID)

    registro.estado = estadosTarea[2][0]
    registro.save()

    return HttpResponseRedirect(reverse('index'))