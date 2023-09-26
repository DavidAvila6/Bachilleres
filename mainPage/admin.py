from django.contrib import admin
from .models import Beca,Facultad,Universidad,Union_U_F,Fundacion,Configuracion_Becas,Becas_Fav,Facultad_fav,Documentos,Requisitos

# Register your models here.

admin.site.register(Beca)
admin.site.register(Facultad)
admin.site.register(Universidad)
admin.site.register(Union_U_F)
admin.site.register(Fundacion)
admin.site.register(Configuracion_Becas)
admin.site.register(Becas_Fav)
admin.site.register(Facultad_fav)
admin.site.register(Documentos)
admin.site.register(Requisitos)