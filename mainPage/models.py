from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Universidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nit = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    class Meta:
        db_table = 'Universidad'
    def __str__(self):
        return self.nombre

class Facultad (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    class   Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_foraneas_Facultad'),
        ]
        db_table = 'Facultad'
    def __str__(self):
        return self.nombre

class Union_U_F(models.Model):
    id = models.AutoField(primary_key=True)
    univeridad = models.ForeignKey(Universidad,on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['univeridad', 'facultad'], name='unique_foraneas_union')
        ]
    def __str__(self):
        fila = "Universidad: "+str(self.univeridad)+" / Facultad: "+str(self.facultad)
        return fila
    
class Fundacion(models.Model):
    id = models.AutoField(primary_key=True)
    Entidad = 'Entidad'
    Universidad = 'Universidad'
    OPCIONES_TIPO = [
        (Entidad, 'Entidad'),
        (Universidad, 'Universidad'),
    ]
    nombre = models.CharField(max_length=30)
    tipo =  models.CharField(max_length=20,choices=OPCIONES_TIPO,default=Universidad)
    def __str__(self):
        return self.nombre
    
class Requisitos (models.Model):
    id = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.Descripcion
    
class Documentos (models.Model):
    id = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.Descripcion
    
class Beca (models.Model):
    id = models.AutoField(primary_key=True)
    Nacional = 'Nacional'
    Extranjera = 'Extranjera'
    OPCIONES_TIPO = [
        (Nacional, 'Nacional'),
        (Extranjera, 'Extranjera'),
    ]
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10,choices=OPCIONES_TIPO,default=Nacional)
    monto = models.IntegerField()
    
    Documentos = models.ManyToManyField(Documentos)
    Requisitos = models.ManyToManyField(Requisitos)
    Descripcion = models.CharField(max_length=1000)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre'], name='unique_foraneas_Beca'),
        ]
        db_table = 'Beca'
    def __str__(self):
        return self.nombre
    
class Configuracion_Becas(models.Model):
    id = models.AutoField(primary_key=True)
    Union_U_F = models.ForeignKey(Union_U_F, on_delete=models.CASCADE)
    Beca = models.ForeignKey(Beca, on_delete=models.CASCADE)
    Fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Union_U_F', 'Beca','Fundacion'], name='unique_foraneas_configuracion')
        ]
    def __str__(self):
        fila = "Union : "+str(self.Union_U_F.univeridad)+"-"+str(self.Union_U_F.facultad)+" / Beca: "+str(self.Beca)+" / Fundacion: "+str(self.Fundacion)
        return fila

    
class Becas_Fav (models.Model):
    id = models.AutoField(primary_key=True)
    facultad = 'facultad'
    beca = 'beca'
    OPCIONES_TIPO = [
        (facultad, 'facultad'),
        (beca, 'beca'),
    ]
    tipo = models.CharField(max_length=10,choices=OPCIONES_TIPO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Configuracion_Becas = models.ForeignKey(Configuracion_Becas, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'Configuracion_Becas','tipo'], name='unique_foraneas_favoritos'),
        ]
    def __str__(self):
        fila = "Tipo : "+str(self.tipo)+" / Usuario: "+str(self.usuario)
        return fila
    
class Facultad_fav(models.Model):
    id = models.AutoField(primary_key=True)
    Facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    Estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Facultad: "+str(self.Facultad)+" / Estudiante: "+str(self.Estudiante)

