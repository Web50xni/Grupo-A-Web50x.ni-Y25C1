from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
#tareas = ['Limpiar', 'Programar', 'Estudiar', 'Barrer']

def index(request):
    # Si la lista de tareas aún no existe, crearla (vacía)
    if "tareas" not in request.session:
        request.session["tareas"] = []

    # Si el método HTTP es POST
    if request.method == 'POST':

        # Si el usuario envía una tarea, almacenarla en el objeto session
        
        nuevaTarea = request.POST.get('tarea')

        # Almacena la string como un elemento de lista, y lo agrega a la lista de tareas. 
        request.session["tareas"] += [nuevaTarea] # Si no se convierte la string a elemento de lista, se agregaría caracter por caracter, lo que no es deseado (así lo maneja python)

        # Refrescar la página para actualizar datos
        return HttpResponseRedirect(reverse('index'))

    # A pesar de que session es un objeto, se comporta como diccionario. Es una implementación llamada 'duck typing', por parte de Python.
    print(f"La sesión es: {request.session}")

    return render(request, 'miApp/index.html', {'tareas': request.session["tareas"]})