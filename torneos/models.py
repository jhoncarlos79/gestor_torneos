from django.db import models
from deportes.models import Deporte
# Create your models here.
class Torneo(models.Model):
    id_torneo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_deporte = models.ForeignKey(Deporte, on_delete=models.SET_NULL, null=True, db_column='id_deporte')

    class Meta:
        managed = False
        db_table = 'torneos'

    def __str__(self):
        return self.nombre