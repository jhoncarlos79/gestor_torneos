from rest_framework import serializers
from resultados.models import Resultado

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ['id_resultados', 'id_partido', 'id_equipo1', 'id_equipo2', 'resultado_equipo1', 'resultado_equipo2']