from django.shortcuts import redirect, render
from django.http import HttpResponse
import mimetypes
import os
from django.contrib.auth.decorators import login_required
from .forms import customUserCreationForm
from .forms import ContactForm
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def principalHub(request):
    return render(request, 'hub.html')

def about(request):
    return render(request, 'about.html')

def recursos(request):
    return render(request, 'recursos.html')
def novedades(request):
    return render(request, 'novedades.html')

def faq(request):
    return render(request, 'faq.html')

def perfil(request):
    return render(request, 'perfil.html')

def Secciones(request):
    return render(request, 'Secciones.html')

def Contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            # Tengo que avisar que todo fue bien
            return redirect(reverse('contact')+'?ok')
        
        else:
            #Tengo que generar un error
            return redirect(reverse('contact')+'?error')   

    return render(request, 'contact.html', {'form':contact_form})





def descargar_archivo(request): 
 
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
 
    filename = 'recursos.txt'
 
    filepath = BASE_DIR + '/AppProyecto/downloads/' + filename 
 
    path = open(filepath, 'r') 
 
    mime_type, _ = mimetypes.guess_type(filepath)
    
    response = HttpResponse(path, content_type = mime_type)
 
    response['Content-Disposition'] = f"attachment; filename={filename}"
 
    return response

def registro(request):
    registro_form = RegistroForm()
    if request.method == 'POST':
        registro_form = RegistroForm(data=request.POST)

        if registro_form.is_valid():
            registro_form.save()
            return redirect(reverse('/')+'?ok')
        
        else:
            return redirect(reverse('registro')+'?error')   

    return render(request, 'registration/registro.html', {'form':registro_form})
    

