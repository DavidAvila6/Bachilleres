from django.shortcuts import redirect, render
from django.http import HttpResponse
import mimetypes
import os
from django.contrib.auth.decorators import login_required
from .forms import customUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
    data = {
        'form': customUserCreationForm()
    }

    if request.method == 'POST':
        formulario = customUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"] )
            login(request, user)
            
            messages.success(request, "Registro exitoso, bienvenido")
            return redirect(to="/")
            
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

