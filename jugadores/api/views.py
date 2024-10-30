from rest_framework.viewsets import ModelViewSet
from jugadores.models import Jugadore
from jugadores.api.serializers import JugadoreSerializer
from jugadores.api.permissions import IsAdminReadOnly

class JugadoreApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=JugadoreSerializer
    queryset = Jugadore.objects.all()
    
