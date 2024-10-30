from rest_framework import serializers
from torneos.models import Torneo

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = ['id_torneo', 'nombre', 'fecha_inicio', 'fecha_fin', 'id_deporte']