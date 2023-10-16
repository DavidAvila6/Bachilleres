from django.contrib import admin
from .models import Beca,Facultad,Universidad,Union_U_F,Fundacion,Configuracion_Becas,Becas_Fav,Facultad_fav,Documentos,Requisitos,Universidad_fav, Publicacion, Comentario, ElegirRespuesta, Pregunta, PreguntasRespondidas, QuizUsuario
from .forms import ElegirInLineFormset
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
admin.site.register(Universidad_fav)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Pregunta)
admin.site.register(ElegirRespuesta)
admin.site.register(PreguntasRespondidas)
admin.site.register(QuizUsuario)

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta','respuesta','correcta','']

    class Meta:
        model = PreguntasRespondidas

class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta.MAXIMO_RESPUESTA
    formset = ElegirInLineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto',]
    search_field = ['texto', 'preguntas__texto']