from rest_framework.viewsets import ModelViewSet
from torneos.models import Torneo
from torneos.api.serializers import TorneoSerializer
from torneos.api.permissions import IsAdminReadOnly

class TorneoApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=TorneoSerializer
    queryset = Torneo.objects.all()
    
