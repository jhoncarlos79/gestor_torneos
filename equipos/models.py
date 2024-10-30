from django.db import models
from users.models import User
from deportes.models import Deporte
from django.utils. html import format_html
# Create your models here.

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column='id_usuario')
    fecha = models.DateTimeField(auto_now=True)
    escudo = models.ImageField(upload_to='equipos', null=True, blank=True)
    id_deporte = models.ForeignKey(Deporte, on_delete=models.SET_NULL, null=True, db_column='id_deporte')

    class Meta:
        managed = False
        db_table = 'equipos'

    def __str__(self):
        return self.nombre

    def mostrar_imagen(self):
        if self.escudo:
            return format_html('<img src="{}" width="50" height="50">'.format(self.escudo.url))
        else:
            return ''
        
    mostrar_imagen.short_description = 'Escudo' # Para que en el administrador no salga el nombre de la funcion sino un nombre del campo