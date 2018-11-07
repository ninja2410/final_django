from django.contrib import admin
from equipos.models import Jugador, JugadorAdmin, Equipo, EquipoAdmin
# Register your models here.
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Equipo, EquipoAdmin)
