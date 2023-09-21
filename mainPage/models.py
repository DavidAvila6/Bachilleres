from django.db import models
from django.forms.widgets import HiddenInput
options = [
    [0, 'Pedido de información'],
    [1, 'Queja por un producto'],
    [2, 'Felicitaciones'],
    [3, 'Otras']
]
Ciudades = [
    [0, 'Bogota-Colombia'],
    [1, 'Medellin-Colombia'],
    [2, 'Cali-Colombia'],
    [3, 'Otras']
]
Area = [
    [0, 'Matematicas'],
    [1, 'Artes'],
    [2, 'Carpintero'],
    [3, 'Otras']
]
class Registro(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre y Apellido')
    email = models.EmailField(verbose_name='Correo electrónico')
    password = models.CharField(max_length=100,
        verbose_name='Password')
    region = models.IntegerField(choices=Ciudades, verbose_name='Ciudad')
    area = models.IntegerField(choices=Area, verbose_name='Area')
    subscription = models.BooleanField(default=False, verbose_name='Suscribirme a correos informativos')
    

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre y Apellido')
    email = models.EmailField(verbose_name='Correo electrónico')
    message = models.TextField(verbose_name='Mensaje')
    contact_type = models.IntegerField(choices=options, verbose_name='Paises')
    subscription = models.BooleanField(default=False, verbose_name='Suscribirme a correos informativos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')
# Create your models here.

