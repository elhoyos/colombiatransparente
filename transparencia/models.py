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
    arriba = models.IntegerField() #default=0?
    abajo = models.IntegerField()
    compartido = models.IntegerField()
    
    def __unicode__(self):
        return self.titulo


class Personaje(models.Model):
    nombre = models.CharField(max_length=64)
    slug = models.SlugField()
    descripcion = models.TextField()
    image = models.ImageField(upload_to='media/img/personajes') #test


class Cargo(models.Model):
    personaje = models.ForeignKey(Personaje)
    titulo = models.CharField(max_length=64)
    inicio = models.DateField()
    terminacion = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('personaje', 'titulo', 'inicio')


class PromesaCargo(models.Model):
    promesa = models.ForeignKey(Promesa)
    cargo = models.ForeignKey(Cargo)


class Etiqueta(models.Model):
    texto = models.CharField(max_length=32, unique=True)
    descripcion = models.TextField()


class PromesaEtiqueta(models.Model):
    promesa = models.ForeignKey(Promesa)
    etiqueta = models.ForeignKey(Etiqueta)
