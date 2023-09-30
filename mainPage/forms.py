from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mainPage.models import Beca

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
            fields = '__all__'