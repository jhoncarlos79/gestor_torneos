from django.db import models

# Create your models here.
class Deporte(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    num_jugadores = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deportes'

    def __str__(self):
        return self.nombre