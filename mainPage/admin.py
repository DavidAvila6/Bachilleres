from django.contrib import admin
from .models import Registro
from .models import Contact

admin.site.register(Registro)
admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_type', 'created_at', 'subscription')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email')
admin.site.unregister(Contact)
admin.site.register(Contact, ContactAdmin)

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'region', 'area', 'subscription')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')
admin.site.unregister(Registro)
admin.site.register(Registro, RegistroAdmin)

# Register your models here.
