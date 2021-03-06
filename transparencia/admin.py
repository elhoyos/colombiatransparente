from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from transparencia.models import *

# Markdown plugin
class MarkItUpWidget(forms.Textarea):
    required = False
    class Media:
        js = (
            'js/libs/jquery-1.5.1.min.js',
            'js/markitup/jquery.markitup.js',
            'js/markitup/sets/markdown/set.js',
            'js/markItUp_init.js',
        )
        css = {
            'screen': (
                'js/markitup/skins/simple/style.css',
                'js/markitup/sets/markdown/style.css',
            )
        }

class PromesaCargoInline(admin.StackedInline):
    model = PromesaCargo
    extra = 0

class PromesaEtiquetaInline(admin.StackedInline):
    model = PromesaEtiqueta
    extra = 0

class PromesaAdminForm(forms.ModelForm):
    descripcion = forms.CharField(widget=MarkItUpWidget())

    class Meta:
        model = Promesa

class PromesaAdmin(admin.ModelAdmin):
    form = PromesaAdminForm
    inlines = [PromesaCargoInline, PromesaEtiquetaInline]
    prepopulated_fields = {"slug": ("titulo",)}


class CargoInline(admin.StackedInline):
    model = Cargo
    extra = 0

class PersonajeAdminForm(forms.ModelForm):
    descripcion = forms.CharField(widget=MarkItUpWidget())

    class Meta:
        model = Personaje

class PersonajeAdmin(admin.ModelAdmin):
    forms = PersonajeAdminForm
    inlines = [CargoInline,]  
    prepopulated_fields = {"slug": ("nombre",)}

class EtiquetaAdminForm(forms.ModelForm):
    descripcion = forms.CharField(widget=MarkItUpWidget())

    class Meta:
        model = Etiqueta

class EtiquetaAdmin(admin.ModelAdmin):
    form = EtiquetaAdminForm

class PerfilColumnistaAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=MarkItUpWidget(), required=False)

    class Meta:
        model = PerfilColumnista

class PerfilColumnistaInline(admin.StackedInline):
    form = PerfilColumnistaAdminForm
    model = PerfilColumnista
    max_num = 1

class UserAdmin(UserAdmin):
    inlines = [PerfilColumnistaInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Promesa, PromesaAdmin)
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
