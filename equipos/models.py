from django.db import models

from django.contrib import admin


class Jugador(models.Model):
    nombre  =   models.CharField(max_length=30)
    procedencia  =   models.CharField(max_length=50)
    dorsal  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()


    def __str__(self):

        return self.nombre


class Equipo(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    jugadores   = models.ManyToManyField(Jugador, through='Partido')

    def __str__(self):

        return self.nombre


class Partido (models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)


class PartidoInLine(admin.TabularInline):
    model = Partido
    extra = 1


class JugadorAdmin(admin.ModelAdmin):
    inlines = (PartidoInLine,)


class EquipoAdmin (admin.ModelAdmin):

    inlines = (PartidoInLine,)
