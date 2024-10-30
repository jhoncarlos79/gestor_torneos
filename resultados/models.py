from django.db import models
from equipos.models import Equipo
from partidos.models import Partido
# Create your models here.
class Resultado(models.Model):
    id_resultados = models.AutoField(primary_key=True)
    id_partido = models.ForeignKey(Partido, on_delete=models.SET_NULL, null=True, db_column='id_partido')
    id_equipo1 = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, db_column='id_equipo1')
    id_equipo2 = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, db_column='id_equipo2', related_name='resultados_id_equipo2_set')
    resultado_equipo1 = models.IntegerField()
    resultado_equipo2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resultados'