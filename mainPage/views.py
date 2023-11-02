import mimetypes
import os
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from AppProyecto import settings
from mainPage.models import Becas_Fav, Configuracion_Becas, Publicacion, Comentario, QuizUsuario, Pregunta, PreguntasRespondidas
from .forms import BecaForm, PublicacionForm, customUserCreationForm
from .forms import EmailForm
from .forms import EmailFormHTML
from .forms import EmailUsername
from .forms import FormularioContacto
from .forms import ArchivoForm
from django.core.mail import send_mail, EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMessage
from .forms import FormularioContacto
from .forms import ComentarioForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.db.models import Count, Prefetch
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import ArchivoForm
from .models import Archivo


from .models import Calificacion
# Create your views here.

@login_required
def calificar(request, estrellas):
    calificacion = Calificacion(usuario=request.user, estrellas=estrellas)
    calificacion.save()
    return redirect('novedades') 


def principalHub(request):
    return render(request, 'hub.html')

def about(request):
    return render(request, 'about.html')

def recursos(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_archivos')  # Redirigir a la vista de lista de archivos
    else:
        form = ArchivoForm()
    return render(request, 'recursos.html', {'form': form})
def novedades(request):
    return render(request, 'novedades.html')
def becasFAV(request):

    becas_sin = Configuracion_Becas.objects.filter(Fundacion__nombre="NA")
    return render(request, 'becas_fav.html', {'becas_sin':becas_sin})

#login_required  

@login_required
def becas(request):
    becas_fun = Configuracion_Becas.objects.distinct("Fundacion")
    for x in becas_fun:
        fundacions = x.Fundacion
        configuracion_unica = Configuracion_Becas.objects.filter(Fundacion=fundacions).values("Union_U_F__univeridad__nombre")
        x.universidades = configuracion_unica
    becas_sin = Configuracion_Becas.objects.filter(Fundacion__nombre="NA")
    becas2 = Configuracion_Becas.objects.all()
    becas = Configuracion_Becas.objects.exclude(Fundacion__nombre="NA")
    return render(request, 'becas.html', {'becas2': becas2,'becas_sin':becas_sin,'becas_fun':becas_fun})


def agregar_beca_fav(request, configuracion_becas_id):
    # Obtener el usuario actual
    usuario = request.user

    # Obtener la configuración de becas
    configuracion_becas = Configuracion_Becas.objects.get(id=configuracion_becas_id)

    # Crear una nueva instancia de Becas_Fav
    beca_fav = Becas_Fav.create(usuario=usuario, configuracion_becas=configuracion_becas)

    # Redirigir a una página de confirmación o a donde prefieras
    return render(request, 'confirmacion.html', {'beca_fav': beca_fav})

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
            if user:
                login(request, user)

                # Renderiza el contenido HTML desde la plantilla
                context = {'user': user}  # Puedes pasar datos adicionales a la plantilla si es necesario
                html_content = render_to_string('correos/emailpage.html', context)


                # Envía un correo electrónico de confirmación con contenido HTML
                subject = 'Bienvenido a Nuestra Aplicación'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [user.email]

                send_mail(subject, '', from_email, recipient_list, fail_silently=True, html_message=html_content)

                

            
            messages.success(request, "Registro exitoso, bienvenido")
            return redirect(to="/")
            
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#Seccion de correos---------------------------------------------------------------------
@login_required
def error_correo(request):
    return render(request, 'correos/error_correo.html')
@login_required
def usuario_noencontrado(request):
    return render(request, 'correos/usuario_noencontrado.html')
@login_required
def correo_enviado(request):
    return render(request, 'correos/correo_enviado.html')

@login_required
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
def correodirecto(request):
    formulario_contacto = EmailUsername()

    if request.method == "POST":
        formulario_contacto = EmailUsername(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            # Busca un usuario por su nombre de usuario
            try:
                usuario = User.objects.get(username=nombre)
                destinatario_email = usuario.email

                email = EmailMessage(
                    "Mensaje de app Django",
                    "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(
                        nombre, email, contenido),
                    '',
                    [destinatario_email],  # Envía el correo al usuario encontrado
                    reply_to=[email]
                )

                try:
                    email.send()
                    return redirect('correo_enviado')
                except Exception as e:
                    # Maneja los errores aquí (por ejemplo, si no se puede conectar al servidor SMTP)
                    print(str(e))
                    return redirect('error_correo')

            except User.DoesNotExist:
                # El nombre de usuario no existe en la base de datos
                # Puedes manejar esta situación de acuerdo a tus necesidades
                return redirect('usuario_noencontrado')

    return render(request, "correos/correo.html", {'miFormulario': EmailUsername})



@login_required
def enviar_correo(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Lista de todos los ususarios
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

@login_required
def enviar_HTML(request):
    if request.method == 'POST':
        form = EmailFormHTML(request.POST)
        if form.is_valid():
            
                subject = form.cleaned_data['subject']
                template_path = os.path.join('mainPage', 'templates', 'correos', 'emailpage.html')
                

                with open(template_path, 'r',encoding='utf-8') as email_template_file:
                    message_html = email_template_file.read()
                
                # Obtén la lista de usuarios registrados
                usuarios_registrados = User.objects.all()

                to_email = [usuario.email for usuario in usuarios_registrados]
                
                # Configura el servidor de correo saliente (SMTP)
                smtp_server = 'smtp.gmail.com'  # Cambia esto si estás usando otro proveedor de correo
                smtp_port = 587  # Puerto de Gmail
                smtp_username = 'bachilleresbch@gmail.com'  # Tu dirección de correo electrónico
                smtp_password = 'qpcu ybch elbk kihu'  # Tu contraseña
                
                send_mail(subject, message_html, smtp_username, to_email, html_message=message_html)
                return redirect('correo_enviado')
    else:
        form = EmailFormHTML()
    
    return render(request, 'correos/enviar_correo.html', {'form': form})
          

#Finalizado Seccion de correos-----------------------------------------------------
#Favoritos------------------------------------
@csrf_exempt
def agregar_favorito(request,beca_id):
    
        
    usuario = request.user  # Obtén el usuario actual
       
        # Asegúrate de tener Configuracion_Becas importado y obtenido correctamente
    configuracion_becas = Configuracion_Becas.objects.get(id=beca_id)

        # Crea la instancia de Becas_Fav y guárdala en la base de datos
    Becas_Fav.create(tipo='becas', usuario=usuario, configuracion_becas=configuracion_becas)

    return redirect('/becas')
#Agregar beca---------------------------
def enviar_correo_beca_agregada(nueva_beca):
    subject = 'Nueva Beca Agregada: {}'.format(nueva_beca.nombre)
    template_name = 'correos/nueva_beca_email.html'

    # Obtén la lista de usuarios registrados
    usuarios_registrados = User.objects.all()
    to_email = [usuario.email for usuario in usuarios_registrados]

    # Configura el servidor de correo saliente (SMTP)
    smtp_server = 'smtp.gmail.com'  # Cambia esto si estás usando otro proveedor de correo
    smtp_port = 587  # Puerto de Gmail
    smtp_username = 'bachilleresbch@gmail.com'  # Tu dirección de correo electrónico
    smtp_password = 'qpcu ybch elbk kihu'  # Tu contraseña

    context = {
        'nombre_beca': nueva_beca.nombre,
        'tipo_beca': nueva_beca.tipo,
        'valor_beca': nueva_beca.valor,
        'descripcion_beca': nueva_beca.Descripcion,
        'requisitos': nueva_beca.Requisitos.all(),
        'documentos': nueva_beca.Documentos.all(),
    }

    message = render(None, template_name, context).content.decode('utf-8')

    send_mail(subject, message, smtp_username, to_email, html_message=message)

def agregar_beca(request):
    if request.method == 'POST':
        form = BecaForm(request.POST)
        if form.is_valid():
            # Guardar la beca
            nueva_beca = form.save()

            # Enviar correo electrónico a los usuarios
            enviar_correo_beca_agregada(nueva_beca)

            return redirect('beca_enviado')
    else:
        form = BecaForm()
    
    return render(request, 'becasform/agregar_beca.html', {'form': form})


@login_required
def beca_enviado(request):
    return render(request, 'becasform/beca_enviado.html')



#FORO JULOX
class PublicacionListView(ListView):
    model = Publicacion
    template_name = 'foro.html'  
    context_object_name = 'publicaciones'
    ordering = ['-fecha_creacion']

    def get_queryset(self):
        # Anotar el número de comentarios por publicación
        queryset = Publicacion.objects.annotate(num_comentarios=Count('comentario'))

        # Usar Prefetch para obtener los comentarios relacionados con cada publicación
        comentarios = Comentario.objects.select_related('autor').all()
        prefetch = Prefetch('comentario_set', queryset=comentarios, to_attr='comentarios')

        # Devolver el queryset con los comentarios precargados
        return queryset.prefetch_related(prefetch)

@login_required   
def agregar_comentario(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = publicacion
            comentario.save()

            # Envía un correo electrónico al autor de la publicación
            subject = 'Nuevo comentario en tu publicación'
            message = f'Se ha agregado un nuevo comentario en tu publicación "{publicacion.titulo}".'
            from_email = settings.EMAIL_HOST_USER  # Usar tu dirección de correo electrónico configurada en settings
            to_email = [publicacion.autor.email]  # El correo electrónico del autor de la publicación
            context = {
                'publicacion_titulo': publicacion.titulo,
                'comentario_autor': comentario.autor.username,
                'comentario_contenido': comentario.contenido,
            }
            html_content = render_to_string('correos/nuevo_comentario.html', context)

            # Envía el correo electrónico con contenido HTML
            send_mail(subject, '', from_email, to_email, fail_silently=True, html_message=html_content)

            return redirect('/foro') 

    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {'publicacion': publicacion, 'form': form})

def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    
    # Verificar que el usuario actual sea el autor del comentario
    if request.user == comentario.autor:
        comentario.delete()
    
    # Redirigir a la página de la publicación a la que pertenece el comentario
    return redirect('/foro', publicacion_id=comentario.publicacion.id)

@login_required   
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save(commit=False)
            nueva_publicacion.autor = request.user
            nueva_publicacion.save()

            
            subject = 'Nueva publicación creada en BCH'
            message = 'Se ha creado una nueva publicación en el apartado de foro en BCH.'
            from_email = settings.EMAIL_HOST_USER 
            to_email = [request.user.email]  

            send_mail(subject, message, from_email, to_email, fail_silently=True)

            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    
    return render(request, 'crear_publicacion.html', {'form': form})

@login_required   
def eliminar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    
    # Verificar que el usuario actual sea el autor de la publicación
    if request.user == publicacion.autor:
        publicacion.delete()
    
    return redirect('/foro/')  # Redirige a la lista de publicaciones

def forosEspecificos(request):
    return render(request, 'foros.html')

#QUIZ Y TEST--------------------------------------------------------------------------------------------------------

def quiz(request):
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuestas_pk = request.POST.get('respuesta_pk')
    else:
        respondidas = PreguntasRespondidas.objects.filter(quizUser=QuizUser).values_list('pregunta__pk', flat=True)
        pregunta = Pregunta.objects.exclude(pk__in=respondidas)

        context={
            'pregunta': pregunta
        }
    return render(request, 'quiz.html', context)


@login_required   
def cargar_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.cleaned_data['id_archivo']
            form = Form(archivo=arhivo)
            print("El formulario es válido. Guardando archivo en la base de datos.")
            form.save()
            return redirect('lista_archivos')
        else:
            print("El formulario no es válido. No se guardará el archivo en la base de datos.")
    else:
        form = ArchivoForm()
    return render(request, 'cargar_archivo.html', {'form': form})

@login_required   
def lista_archivos(request):
    archivos = Archivo.objects.all()
    return render(request, 'lista_archivos.html', {'archivos': archivos})


