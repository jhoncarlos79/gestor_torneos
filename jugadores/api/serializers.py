from rest_framework import serializers
from jugadores.models import Jugadore

class JugadoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugadore
        fields = ['id_jugador', 'nombre', 'fecha_nacimiento', 'estatura','peso', 'id_equipo', 'fecha_vinculacion', 'foto']