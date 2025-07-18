from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Tu Nombre', max_length=100)
    correo = forms.EmailField(label='Correo Electrónico')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre.split()) < 2:
            raise forms.ValidationError("Por favor, ingresa tu nombre completo.")
        return nombre
    
class SupportForm(forms.Form):
    nombre = forms.CharField(label='Tu Nombre', max_length=100)
    correo = forms.EmailField(label='Correo Electrónico')
    problema = forms.ChoiceField(choices=[
        ('login', 'Problemas de inicio de sesión'),
        ('pago', 'Problemas de pago'),
        ('bug', 'Error o bug'),
        ('otro', 'Otro')
    ])
    descripcion = forms.CharField(label='Descripción del problema', widget=forms.Textarea)
    urgente = forms.BooleanField(label='¿Es urgente?', required=False)

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion