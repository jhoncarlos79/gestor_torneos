from rest_framework import serializers
from partidos.models import Partido

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ['id_partido', 'fecha', 'hora', 'lugar', 'id_torneo', 'id_equipo1', 'id_equipo2', 'resultado_equipo1', 'resultado_equipo2']