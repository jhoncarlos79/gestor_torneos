from django.contrib import admin
from equipos.models import Equipo
# Register your models here.

@admin.register(Equipo)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'mostrar_imagen', 'id_usuario', 'id_deporte']


