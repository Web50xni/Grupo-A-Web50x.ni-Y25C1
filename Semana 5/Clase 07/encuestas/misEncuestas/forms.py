from django import forms

class formHTML(forms.Form):
    concepto = forms.CharField(label="¿Qué es HTML?", max_length=200, widget=forms.TextInput(attrs={'class': 'inputs-large', 'placeholder': 'Escribe el concepto.'}))
    iniciales = forms.ChoiceField(label="¿A qué hace referencia HTML?", choices=[
        ("iniciales_op1", "Hypertext Markup Language"),
        ("iniciales_op2", "HTTP Markup Language"),
        ("iniciales_op3", "Hypertext Mark Language"),
        ("iniciales_op4", "Hypercarry Tryndramere Platinum")
        ], widget=forms.RadioSelect # Indica que el campo es un input:radio, sin esto, es un select
        )
    
    etiquetaHead = forms.MultipleChoiceField(label="La etiqueta HTML permite...", choices=[
        ("head_op1", "Indicar metadatos."),
        ("head_op2", "Enlazar archivos."),
        ("head_op3", "Escribir código del cuerpo de página."),
        ("head_op4", "Ajua"),
    ], widget=forms.CheckboxSelectMultiple)

    etiquetaAnchor = forms.ChoiceField(label="Permite establecer un hipervínculo en una página web.", choices=[
        ("<a>", "Etiqueta <a>"),
        ("<i>", "Etiqueta <i>"),
        ("src", "Parámetro src=''"),
        ("<link>", "Etiqueta <link>")
    ], widget=forms.RadioSelect)

    cantidadParrafos = forms.IntegerField(label="¿Cuántas etiquetas <p> se imprimirán con la siguiente abreviación Emmet en VSCode?", widget=forms.NumberInput(attrs={
        'class': 'inputs-large',
        'placeholder': 'Ingresa la cantidad',
        'min': 0
        }))