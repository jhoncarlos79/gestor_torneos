from django.contrib import admin
from partidos.models import Partido
# Register your models here.

@admin.register(Partido)

class PartidoAdmin(admin.ModelAdmin):
    list_display=['id_partido', 'fecha', 'hora', 'lugar', 'id_torneo', 'id_equipo1', 'resultado_equipo1', 'id_equipo2', 'resultado_equipo2']