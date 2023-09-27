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
from django.contrib import admin
from django.urls import path, include
from mainPage import views
from AppProyecto.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principalHub),
    path('about/', views.about),
    path('recursos/', views.recursos),
    path('novedades/', views.novedades),
    path('Medicina/', views.Medicina),
    path('faq/', views.faq),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Secciones/', views.Secciones ),
    path('perfil/', views.perfil ),
    path('edit_perfil/', views.edit_perfil, name='edit_perfil'),
    #Correos-----------------------------------------------------------------
    path('correo/', views.correo,name='correo'),
    path('correodirecto/', views.correodirecto,name='correodirecto'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('error_correo/', views.error_correo, name='error_correo'),
    path('usuario_noencontrado/', views.usuario_noencontrado, name='usuario_noencontrado'),
    path('correo_enviado/', views.correo_enviado, name='correo_enviado'),
    path('enviar_HTML/', views.enviar_HTML,name='enviar_HTML'),

    path('descargar/', views.descargar_archivo, name = "descargar"),
    path('registro/', views.registro, name="registro")
    
    
]
