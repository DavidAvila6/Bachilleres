from django.db import models
from schedule.models import Event

class EventoCalendario(Event):
    descripcion = models.TextField()

# Create your models here.
