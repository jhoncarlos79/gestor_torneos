from rest_framework import serializers
from equipos.models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id_equipo', 'nombre', 'id_usuario', 'fecha', 'escudo', 'id_deporte']