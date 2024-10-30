from django.contrib import admin
from deportes.models import Deporte
# Register your models here.
# Enviar al panel de administracion el modelo

@admin.register(Deporte)

class DeporteAdmin(admin.ModelAdmin):
    list_display = ['nombre','num_jugadores']
