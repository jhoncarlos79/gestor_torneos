from rest_framework.viewsets import ModelViewSet
from deportes.models import Deporte
from deportes.api.serializers import DeporteSerializer
#añadir los permisos
from deportes.api.permissions import IsAdminReadOnly

class DeporteApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=DeporteSerializer
    queryset = Deporte.objects.all()
    
