from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from transparencia.models import *

class PerfilInline(admin.StackedInline):
    model = PerfilColumnista
    max_num = 1

class UserAdmin(UserAdmin):
    inlines = [PerfilInline,]

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

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Promesa, PromesaAdmin)
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Etiqueta)
