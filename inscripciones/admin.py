from django.contrib import admin
from inscripciones.models import Incripcione
# Register your models here.

@admin.register(Incripcione)

class InscripcioneAdmin(admin.ModelAdmin):
    list_display = ['id_equipo', 'id_torneo', 'fecha_inscripcion']