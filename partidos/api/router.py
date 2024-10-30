from rest_framework.routers import DefaultRouter
from partidos.api.views import PartidoApiViewSet

router_partidos = DefaultRouter()
router_partidos.register(prefix='partidos', basename='partidos', viewset=PartidoApiViewSet)