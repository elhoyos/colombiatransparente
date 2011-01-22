from django.db import models

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
    slug = models.SlugField()
    estatus = models.IntegerField(choices=ESTATUS_OPCIONES)
    descripcion = models.TextField()
    arriba = models.IntegerField(default=0)
    abajo = models.IntegerField(default=0)
    compartido = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.titulo

class Personaje(models.Model):
    nombre = models.CharField(max_length=64)
    slug = models.SlugField()
    descripcion = models.TextField()
    image = models.ImageField(upload_to='img/personajes')

    def __unicode__(self):
        return self.nombre

class Cargo(models.Model):
    personaje = models.ForeignKey(Personaje)
    titulo = models.CharField(max_length=64)
    inicio = models.DateField()
    terminacion = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s, %s, %s - %s" % (self.personaje.nombre, self.titulo, self.inicio.year, self.terminacion.year)

    class Meta:
        unique_together = ('personaje', 'titulo', 'inicio')

class PromesaCargo(models.Model):
    promesa = models.ForeignKey(Promesa)
    cargo = models.ForeignKey(Cargo)

class Etiqueta(models.Model):
    texto = models.CharField(max_length=32, unique=True)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.texto

class PromesaEtiqueta(models.Model):
    promesa = models.ForeignKey(Promesa)
    etiqueta = models.ForeignKey(Etiqueta)
