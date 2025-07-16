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
    
class formCSS(forms.Form):
    selector = forms.ChoiceField(label="¿Cuál es un selector válido en CSS?", choices=[
        ("css_op1", ".clase"),
        ("css_op2", "@media"),
        ("css_op3", "body:hover"),
        ("css_op4", "<selector>"),
    ], widget=forms.RadioSelect)

    propiedadColor = forms.CharField(label="¿Qué propiedad se usa para cambiar el color del texto?", max_length=100,
        widget=forms.TextInput(attrs={'class': 'inputs-large', 'placeholder': 'Ej: color'}))

    valoresDisplay = forms.MultipleChoiceField(label="¿Cuáles son valores válidos de la propiedad display?", choices=[
        ("disp1", "block"),
        ("disp2", "flex"),
        ("disp3", "grid"),
        ("disp4", "transparent"),
    ], widget=forms.CheckboxSelectMultiple)

    unidadMedida = forms.ChoiceField(label="¿Cuál de las siguientes NO es una unidad válida de medida en CSS?", choices=[
        ("css_unit1", "rem"),
        ("css_unit2", "px"),
        ("css_unit3", "vh"),
        ("css_unit4", "grs"),
    ], widget=forms.RadioSelect)

    importancia = forms.ChoiceField(label="¿Qué indica `!important` en una declaración CSS?", choices=[
        ("imp1", "Es un comentario"),
        ("imp2", "Importa otro archivo"),
        ("imp3", "Sobrescribe otras reglas"),
        ("imp4", "Define prioridad de carga"),
    ], widget=forms.RadioSelect)



class formGit(forms.Form):
    comando_inicializar = forms.ChoiceField(label="¿Cual es el comando para inicializar un repositorio local¿", choices=[
    ('git_opc1', "git init"),
    ('git_opc2', "git start"),
    ('git_opc3', "git create"),
    ], widget=forms.RadioSelect
    )
















