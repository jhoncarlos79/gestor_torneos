from django.db import models
from torneos.models import Torneo
from equipos.models import Equipo

# Create your models here.
class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.SET_NULL, null=True, db_column='id_torneo')
    id_equipo1 = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, db_column='id_equipo1')
    id_equipo2 = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, db_column='id_equipo2', related_name='resultados_id_equipo2_set')
    resultado_equipo1 = models.IntegerField()
    resultado_equipo2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partidos'

    def __str__(self):
        return str(self.id_partido) + " - " + str(self.fecha) + " - " + str(self.hora) + " - " + self.lugar