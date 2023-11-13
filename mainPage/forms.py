from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  mainPage.models import Comentario
from .models import Archivo



from mainPage.models import Beca, Publicacion, Pregunta, ElegirRespuesta, PreguntasRespondidas,Oportunidad

class customUserCreationForm(UserCreationForm):
    
    birthdate = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','birthdate']

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class EmailFormHTML(forms.Form):#Form para enviar HTML
    subject = forms.CharField(max_length=100)


class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=20)
    email=forms.CharField(label='Email', required=True, max_length=30)
    contenido=forms.CharField(label='Contenido', max_length=400, widget=forms.Textarea )

class EmailUsername(forms.Form):
    nombre=forms.CharField(label='Username', required=True, max_length=20)
    contenido=forms.CharField(label='Contenido', max_length=400, widget=forms.Textarea )

    #nueva beca------------------
class BecaForm(forms.ModelForm):
        class Meta:
            model = Beca
            fields = ['nombre', 'tipo', 'valor_duracion'
                      , 'Documentos', 'Requisitos', 'Descripcion']

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

class ElegirInLineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInLineFormset, self).clean()

        respuesta_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return 

            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1 

        try:
            assert respuesta_correcta == Pregunta.NUMERO_DE_RESPUESTAS_PERMITIDAS           
        except AssertionError:
            raise forms.ValidationError('Exactamente solo una respuesta es permitida')
        
class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'archivo']


class OportunidadForm(forms.ModelForm):
    etiquetas_materias = forms.MultipleChoiceField(
        choices=[
            ('matematicas', 'Matemáticas'),
            ('medicina', 'Medicina'),
            ('economia', 'Economía'),
            ('otro', 'Otro'),
            # Añade más etiquetas según sea necesario
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Permitir etiquetas vacías
    )
    etiquetas_tipo = forms.MultipleChoiceField(
        choices=[
            ('carrera', 'Carrera'),
            ('beca', 'Beca'),
            ('pasantia', 'Pasantia'),
            ('trabajo', 'Trabajo'),
            ('otro', 'Otro'),
            # Añade más etiquetas según sea necesario
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Permitir etiquetas vacías
    )
    def clean_etiquetas_materias(self):
        etiquetas_materias = self.cleaned_data.get('etiquetas_materias')
        return ','.join(etiquetas_materias) if etiquetas_materias else None

    def clean_etiquetas_tipo(self):
        etiquetas_tipo = self.cleaned_data.get('etiquetas_tipo')
        return ','.join(etiquetas_tipo) if etiquetas_tipo else None    

    class Meta:
        model = Oportunidad
        fields = ['titulo', 'contenido', 'etiquetas_materias', 'etiquetas_tipo', 'imagen']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'container-ui'}),
            'contenido': forms.Textarea(attrs={'class': 'container-ui'}),
            'etiquetas_materias': forms.CheckboxSelectMultiple(attrs={'class': 'mi-clase-estilo'}),
            'etiquetas_tipo': forms.CheckboxSelectMultiple(attrs={'class': 'mi-clase-estilo'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'mi-clase-estilo'}),
        }
