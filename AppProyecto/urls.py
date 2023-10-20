import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainPage import views
from AppProyecto.settings import BASE_DIR


urlpatterns = [
    # Chat-------
    path('', include('chat.urls')),

    # MainPage-----------
    path('admin/', admin.site.urls),
    path('', views.principalHub),
    path('about/', views.about),
    path('recursos/', views.recursos),
    path('novedades/', views.novedades),
    path('becas/', views.becas),
    path('faq/', views.faq),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Secciones/', views.Secciones),
    path('perfil/', views.perfil),
    path('edit_perfil/', views.edit_perfil, name='edit_perfil'),
    #becas fav en perfil--------------------------------------------------------
    # path('becas_fav/', views.becasFAV, name='becas_fav'),
    path('becas_fav/', views.becasFAV, name='becas_fav'),
    # ...
     path('calificar/<int:estrellas>/', views.calificar, name='calificar'),

    #-------

    # Correos-----------------------------------------------------------------
    path('correo/', views.correo, name='correo'),
    path('correodirecto/', views.correodirecto, name='correodirecto'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('error_correo/', views.error_correo, name='error_correo'),
    path('usuario_noencontrado/', views.usuario_noencontrado,
         name='usuario_noencontrado'),
    path('agregar_favorito/', views.agregar_favorito,
         name='nombre_de_tu_vista_agregar_favorito'),
    path('correo_enviado/', views.correo_enviado, name='correo_enviado'),
    path('enviar_HTML/', views.enviar_HTML, name='enviar_HTML'),

    path('descargar/', views.descargar_archivo, name="descargar"),
    path('registro/', views.registro, name="registro"),
    path('agregar_favorito/<int:beca_id>/', views.agregar_favorito,
         name='nombre_de_tu_vista_agregar_favorito'),
    path('agregar_beca/', views.agregar_beca, name='agregar_beca'),
    path('beca_enviado/', views.beca_enviado, name='beca_enviado'),
    
    #Calendario----------------------------------------------------------------------------------------------------------------------------------
    path('perfil/calendar/', include('cal.urls')),
    
    #foro----------------------------------------------------------------------------------------------------------------------------------
    path('foro/', views.PublicacionListView.as_view(), name='lista_publicaciones'),
    path('foro/<int:publicacion_id>/agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('foro/comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('foro/crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('foro/publicacion/<int:publicacion_id>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('foro/forosFacultades/', views.forosEspecificos,name='foros_especificos'),
    #Quices y TEST----------------------------------------------------------------------------------------------------------------------------------
    path('quiz/', views.quiz ,name='quices')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
