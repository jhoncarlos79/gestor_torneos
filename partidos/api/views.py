from rest_framework.viewsets import ModelViewSet
from partidos.models import Partido
from partidos.api.serializers import PartidoSerializer
from partidos.api.permissions import IsAdminReadOnly

class PartidoApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=PartidoSerializer
    queryset = Partido.objects.all()