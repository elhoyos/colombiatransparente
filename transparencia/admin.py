from django.contrib import admin
from django.contrib import admin

from transparencia.models import Promesa, Personaje, Cargo, PromesaCargo, Etiqueta, PromesaEtiqueta

class PromesaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

class PersonajeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Promesa, PromesaAdmin)
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Cargo)
admin.site.register(PromesaCargo)
admin.site.register(Etiqueta)
admin.site.register(PromesaEtiqueta)
