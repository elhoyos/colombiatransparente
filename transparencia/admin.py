from django.contrib import admin
from django.contrib import admin

from transparencia.models import Promesa, Personaje, Cargo, PromesaCargo, Etiqueta, PromesaEtiqueta

class PromesaCargoInline(admin.StackedInline):
    model = PromesaCargo
    extra = 1

class PromesaEtiquetaInline(admin.StackedInline):
    model = PromesaEtiqueta
    extra = 1

class PromesaAdmin(admin.ModelAdmin):
    inlines = [PromesaCargoInline, PromesaEtiquetaInline]
    prepopulated_fields = {"slug": ("titulo",)}

class CargoInline(admin.StackedInline):
    model = Cargo
    extra = 1

class PersonajeAdmin(admin.ModelAdmin):
    inlines = [CargoInline,]  
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Promesa, PromesaAdmin)
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Etiqueta)
