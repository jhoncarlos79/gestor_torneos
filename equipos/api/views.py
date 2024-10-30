from rest_framework.viewsets import ModelViewSet
from equipos.models import Equipo
from equipos.api.serializers import EquipoSerializer
from equipos.api.permissions import IsAdminReadOnly

class EquipoApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=EquipoSerializer
    queryset = Equipo.objects.all()