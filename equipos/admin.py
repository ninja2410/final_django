from django.contrib import admin
from peliculas.models import Jugador, JugadorAdmin, Equipo, EquipoAdmin
# Register your models here.
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Equipo, EquipoAdmin)
