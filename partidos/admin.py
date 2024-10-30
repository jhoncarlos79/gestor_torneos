from django.contrib import admin
from partidos.models import Partido
# Register your models here.

@admin.register(Partido)

class PartidoAdmin(admin.ModelAdmin):
    list_display=['id_partido', 'fecha', 'hora', 'lugar', 'id_torneo']