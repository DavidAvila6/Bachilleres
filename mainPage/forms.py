from django import forms
from .models import Contact
from .models import Registro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class customUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ContactForm(forms.ModelForm):
    
    class Meta:
         model = Contact
         fields = '__all__'
            

class RegistroForm(forms.ModelForm):
    
    class Meta:
         model = Registro
         fields = '__all__'
         widgets = {
            'password': forms.PasswordInput(),
        }         
        