from django.contrib import admin
from torneos.models import Torneo
# Register your models here.
@admin.register(Torneo)

class TorneoAdmin(admin.ModelAdmin):
    list_display=['nombre', 'fecha_inicio', 'fecha_fin', 'id_deporte']