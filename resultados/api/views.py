from rest_framework.viewsets import ModelViewSet
from resultados.models import Resultado
from resultados.api.serializers import ResultadoSerializer
from resultados.api.permissions import IsAdminReadOnly

class ResultadoApiViewSet(ModelViewSet):
    permission_classes=[IsAdminReadOnly]
    serializer_class=ResultadoSerializer
    queryset = Resultado.objects.all()
    
