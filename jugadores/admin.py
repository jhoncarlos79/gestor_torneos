from django.contrib import admin
from jugadores.models import Jugadore
# Register your models here.

@admin.register(Jugadore)

class JugadoreAdmin(admin.ModelAdmin):
    list_display=['mostrar_imagen', 'nombre', 'fecha_nacimiento', 'estatura', 'peso', 'id_equipo', 'fecha_vinculacion']