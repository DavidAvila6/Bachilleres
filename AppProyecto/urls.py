"""AppProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainPage import views
from AppProyecto.settings import BASE_DIR
from django.urls import path
from mainPage .views import guardar_oportunidad


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principalHub),
    path('about/', views.about),
    path('recursos/', views.recursos),
    path('novedades/', views.novedades),
    path('becas/',views.becas),
    path('faq/', views.faq),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Secciones/', views.Secciones ),
    path('lista_archivos/', views.lista_archivos ),
    path('perfil/', views.perfil ),
    path('edit_perfil/', views.edit_perfil, name='edit_perfil'),
    #becas fav en perfil--------------------------------------------------------
    # path('becas_fav/', views.becasFAV, name='becas_fav'),
    path('becas_fav/', views.becasFAV, name='becas_fav'),
    # ...
     path('calificar/<int:estrellas>/', views.calificar, name='calificar'),

    #-------

    #Correos-----------------------------------------------------------------
    path('correo/', views.correo,name='correo'),
    path('correodirecto/', views.correodirecto,name='correodirecto'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('error_correo/', views.error_correo, name='error_correo'),
    path('usuario_noencontrado/', views.usuario_noencontrado, name='usuario_noencontrado'),
    path('agregar_favorito/', views.agregar_favorito, name='nombre_de_tu_vista_agregar_favorito'),
    path('correo_enviado/', views.correo_enviado, name='correo_enviado'),
    path('enviar_HTML/', views.enviar_HTML,name='enviar_HTML'),

    path('descargar/', views.descargar_archivo, name = "descargar"),
    path('registro/', views.registro, name="registro"),
    path('agregar_favorito/<int:beca_id>/', views.agregar_favorito, name='nombre_de_tu_vista_agregar_favorito'),
    path('agregar_beca/', views.agregar_beca, name='agregar_beca'),
    path('beca_enviado/', views.beca_enviado, name='beca_enviado'),
    
    #Calendario----------------------------------------------------------------------------------------------------------------------------------
    path('perfil/calendar/', include('cal.urls')),
    
    #foro----------------------------------------------------------------------------------------------------------------------------------
    path('foro/', views.PublicacionListView.as_view(), name='lista_publicaciones'),
    path('foro/<int:publicacion_id>/agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('foro/comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('foro/crear_publicacion/<int:facultad_id>/', views.crear_publicacion, name='crear_publicacion'),
    path('foro/publicacion/<int:publicacion_id>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('foro/forosFacultades/', views.forosEspecificos,name='foros_especificos'),
    path('foro/facultad/<int:facultad_id>/', views.foro_por_facultad, name='foro_por_facultad'),
    #Quices y TEST----------------------------------------------------------------------------------------------------------------------------------
    path('quiz/', views.quiz ,name='quices'),
    path('cargar-archivo/', views.cargar_archivo, name='cargar_archivo'),
    path('lista-archivos/', views.lista_archivos, name='lista_archivos'),
    #Oportunidades--------------------
    path('oportunidades/', views.oportunidades, name='oportunidades'),
    path('crear_oportunidad/', views.crear_oportunidad, name='crear_oportunidad'),
    path('cargar_mas_oportunidades/', views.cargar_mas_oportunidades, name='cargar_mas_oportunidades'),
    path('filtrar_oportunidades/', views.filtrar_oportunidades, name='filtrar_oportunidades'),
    path('guardar_oportunidad/', views.guardar_oportunidad, name='guardar_oportunidad'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)