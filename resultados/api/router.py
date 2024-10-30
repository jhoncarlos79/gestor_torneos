from rest_framework.routers import DefaultRouter
from resultados.api.views import ResultadoApiViewSet

router_resultados = DefaultRouter()
router_resultados.register(prefix='resultados', basename='resultados', viewset=ResultadoApiViewSet)