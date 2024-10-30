from rest_framework import serializers
from inscripciones.models import Incripcione

class IncripcioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incripcione
        fields = ['id_inscripciones', 'id_equipo', 'id_torneo', 'fecha_inscripcion']