import mimetypes
import os
import smtplib
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import customUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import EmailForm
from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMessage
from .forms import FormularioContacto

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

@login_required
def edit_perfil(request):
    if request.method == 'POST':
        form = customUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/perfil')  
    else:
        form = customUserCreationForm(instance=request.user)
    
    return render(request, 'edit_perfil.html', {'form': form})





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

#Seccion de correos---------------------------------------------------------------------
def error_correo(request):
    return render(request, 'correos/error_correo.html')

def correo_enviado(request):
    return render(request, 'correos/correo_enviado.html')

def correo(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
            '',
            ["bachilleresbch@gmail.com"], 
            reply_to=[email])

            try:
                email.send()

                return redirect('correo_enviado')
            except Exception as e:
                # Maneja los errores aquí (por ejemplo, si no se puede conectar al servidor SMTP)
                print(str(e))
                return redirect('error_correo')

    return render(request, "correos/correo.html", {'miFormulario':formulario_contacto})

@login_required
def enviar_correo(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Obtén la lista de usuarios registrados
            usuarios_registrados = User.objects.all()

            to_email = [usuario.email for usuario in usuarios_registrados]
            
            # Configura el servidor de correo saliente (SMTP)
            smtp_server = 'smtp.gmail.com'  # Cambia esto si estás usando otro proveedor de correo
            smtp_port = 587  # Puerto de Gmail
            smtp_username = 'bachilleresbch@gmail.com'  # Tu dirección de correo electrónico
            smtp_password = 'qpcu ybch elbk kihu'  # Tu contraseña
            
            # Configura el mensaje
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            
            # Inicia la conexión con el servidor SMTP de Gmail
            try:
                send_mail(subject, message, smtp_username, to_email, fail_silently=False)
                return redirect('correo_enviado') 
            except Exception as e:
                # Maneja los errores aquí (por ejemplo, si no se puede conectar al servidor SMTP)
                print(str(e))
                return redirect('error_correo')  # Redirige a una página de error
    else:
        form = EmailForm()
    
    return render(request, 'correos/enviar_correo.html', {'form': form})

#Finalizado Seccion de correos-----------------------------------------------------