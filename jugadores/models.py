from django.db import models
from equipos.models import Equipo
from django.utils. html import format_html

# Create your models here.
class Jugadore(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    estatura = models.FloatField()
    peso = models.IntegerField()
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, db_column='id_equipo')
    fecha_vinculacion = models.DateTimeField()
    foto = models.ImageField(upload_to='jugadores', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'jugadores'

    def mostrar_imagen(self):
        if self.foto:
            return format_html('<img src="{}" width="50" height="50">'.format(self.foto.url))
        else:
            return ''
        
    mostrar_imagen.short_description = 'Foto'