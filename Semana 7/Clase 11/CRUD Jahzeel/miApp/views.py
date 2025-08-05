from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Tarea
from django.urls import reverse


# Create your views here.
def index(request):

    if request.method == 'POST':
        contenido = request.POST.get('contenido')

        nuevaTarea = Tarea.objects.create(contenido=contenido)
        nuevaTarea.save()

        return HttpResponseRedirect(reverse('index'))

    tareas = Tarea.objects.all()

    return render(request, 'miApp/index.html', {
        'tareas': tareas
    })

def eliminar(request, ID):

    datoEliminar = get_object_or_404(Tarea, id=ID)

    datoEliminar.delete()

    return HttpResponseRedirect(reverse('index'))