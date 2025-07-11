from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import formHTML

# Create your views here.
def index(request):

    return render(request, 'misEncuestas/index.html', {})

def encuesta(request, tema):
    # Utilizada en método GET
    form = formHTML()

    if request.method == "POST":
        # Utilizado en método POST
        form = formHTML(request.POST)

        if form.is_valid():
            print("Los datos enviados fueron: ")
            for campo, valor in form.cleaned_data.items():
                print(f"{campo}: {valor}")

            # Refresca la página
            return HttpResponseRedirect(reverse('encuestas', kwargs={'tema': tema}))

        else:
            # Refrescar y enviar mensaje de error
            return HttpResponseRedirect(reverse('encuestas', kwargs={'tema': tema, 'mensaje': 'Formulario Inválido'}))



    

    return render(request, 'misEncuestas/encuesta.html', {
        'tema': tema,
        'form': form
    })