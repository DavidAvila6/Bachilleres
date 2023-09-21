from django import forms
from .models import Contact
from .models import Registro
from django.contrib.auth.forms import UserCreationForm

class customUserCreationForm(UserCreationForm):
    pass
