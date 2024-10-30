from rest_framework import serializers
from deportes.models import Deporte

class DeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deporte
        fields = ['id_deporte', 'nombre', 'num_jugadores']