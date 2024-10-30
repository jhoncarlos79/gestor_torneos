from rest_framework.viewsets import ModelViewSet
from inscripciones.models import Incripcione
from inscripciones.api.serializers import IncripcioneSerializer
from inscripciones.api.permissions import IsAdminReadOnly

class IncripcioneApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=IncripcioneSerializer
    queryset = Incripcione.objects.all()