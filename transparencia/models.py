from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from sorl import thumbnail


class PerfilColumnista(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    bio = models.TextField(blank=True, null=True)
    image = thumbnail.ImageField(upload_to='img/columnistas', blank=True, null=True)

def crear_perfil_columnista(sender, instance, created, **kwargs):
    if created:
        perfil = PerfilColumnista()
        perfil.user = instance
        perfil.save()

post_save.connect(crear_perfil_columnista, sender=User)


ESTANCADO = 0
EN_PROCESO = 1
INCUMPLIDA = 2
A_MEDIAS = 3
CUMPLIDA = 4

ESTATUS_OPCIONES = (
    (ESTANCADO, "Estancado"),
    (EN_PROCESO, "En Proceso"),
    (INCUMPLIDA, "Incumplida"),
    (A_MEDIAS, "A Medias"),
    (CUMPLIDA, "Cumplida"),
)

class Promesa(models.Model):
    titulo = models.CharField(max_length=200)
    columnista = models.ForeignKey(User)
    actualizado = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    estatus = models.IntegerField(choices=ESTATUS_OPCIONES)
    descripcion = models.TextField()
    arriba = models.IntegerField(default=0, editable=False)
    abajo = models.IntegerField(default=0, editable=False)
    compartido = models.IntegerField(default=0, editable=False)
    
    def __unicode__(self):
        return self.titulo

class Personaje(models.Model):
    nombre = models.CharField(max_length=64)
    columnista = models.ForeignKey(User)
    actualizado = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    descripcion = models.TextField()
    image = thumbnail.ImageField(upload_to='img/personajes')

    def __unicode__(self):
        return self.nombre

class Cargo(models.Model):
    personaje = models.ForeignKey(Personaje)
    titulo = models.CharField(max_length=64)
    actual = models.BooleanField()
    inicio = models.DateField()
    terminacion = models.DateField(blank=True, null=True)

    def __unicode__(self):
        if self.terminacion:
            return "%s, %s, %s - %s" % (self.personaje.nombre, self.titulo, self.inicio.year, self.terminacion.year)
        else:
            return "%s, %s, %s" % (self.personaje.nombre, self.titulo, self.inicio.year)

    class Meta:
        unique_together = (
            ('personaje', 'titulo', 'inicio',),
        )

class PromesaCargo(models.Model):
    promesa = models.ForeignKey(Promesa)
    cargo = models.ForeignKey(Cargo)

class Etiqueta(models.Model):
    columnista = models.ForeignKey(User)
    actualizado = models.DateTimeField(auto_now=True)
    texto = models.CharField(max_length=32, unique=True)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.texto

    def save(self):
        self.texto = self.texto.lower()
        super(Etiqueta, self).save()

class PromesaEtiqueta(models.Model):
    promesa = models.ForeignKey(Promesa)
    etiqueta = models.ForeignKey(Etiqueta)
