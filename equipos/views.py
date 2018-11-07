from django.shortcuts import render
from django.contrib import messages
from .forms import EquipoForm
from Equipos.models import Equipo, Partido

def Equipo_nueva(request):
    if request.method == "POST":
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            Equipo = Equipo.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for Jugador_id in request.POST.getlist('Jugadores'):
                partido = Partido(Jugador_id=Jugador_id, Equipo_id = Equipo.id)
                partido.save()
            messages.add_message(request, messages.SUCCESS, 'Equipo guardado Exitosamente')
    else:
        formulario = EquipoForm()
    return render(request, 'equipos/equiepo_editar.html', {'formulario': formulario})
