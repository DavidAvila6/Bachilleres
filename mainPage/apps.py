from django.apps import AppConfig


class MainpageConfig(AppConfig):
    name = 'mainPage'

class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Registro'  
    verbose_name = 'Usarios Registrados'

class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Contact'
    verbose_name = 'Mensajes de Contacto'    
