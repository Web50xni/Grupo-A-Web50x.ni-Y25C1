from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, SupportForm
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'Ayuda/layout.html'

class ContactFormView(FormView):
    template_name = 'Ayuda/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('gracias')

    def form_valid(self, form):
        print("Contacto Rebido: ", form.cleaned_data)
        return super().form_valid(form)
    
class SupportFormView(FormView):
    template_name = 'Ayuda/support_form.html'
    form_class = SupportForm
    success_url = reverse_lazy('gracias')

    def form_valid(self, form):
        data = form.cleaned_data
        if data['urgente']:
            print("Soporte Urgente: ", data)
        else:
            print("Soporte Normal: ", data)
        return super().form_valid(form)
    
class GraciasView(TemplateView):
    template_name = 'Ayuda/thank_you.html'