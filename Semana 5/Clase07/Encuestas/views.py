from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import formHTML, formCSS, formGit

# Create your views here.
def index(request):

    return render(request, 'index.html', {})

def encuesta(request, tema):
    # Utilizada en método GET
    form = None

    if tema == "HTML":
        form = formHTML()
    elif tema == "CSS":
        form = formCSS()
    elif tema == "Git":
        form = formGit()

    if request.method == "POST":
       
        conceptoHTML = request.POST.get('iniciales_op1')
        referenciaHTML = request.POST.get('op1HTML')
        entero = request.POST.get('interInput')
        miFORM = request.POST.get('HTML')

        print(conceptoHTML, referenciaHTML, entero, miFORM)

        return HttpResponseRedirect(reverse('encuestas', kwargs = {'tema': tema})) # ../index/encestas



    # Renderiza la plantilla con el formulario
    return render(request, 'encuesta.html', {
        'tema': tema,
        'form': form,
    })