from django.db import models
from equipos.models import Equipo
from torneos.models import Torneo
# Create your models here.
class Incripcione(models.Model):
    id_inscripciones = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, db_column='id_equipo')
    id_torneo = models.ForeignKey(Torneo, on_delete=models.SET_NULL, null=True, db_column='id_torneo')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'incripciones'