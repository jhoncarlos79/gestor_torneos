from django.contrib import admin
from resultados.models import Resultado
# Register your models here.

@admin.register(Resultado)

class ResultadoAdmin(admin.ModelAdmin):
    list_display=['id_partido', 'id_equipo1', 'resultado_equipo1', 'id_equipo2', 'resultado_equipo2']