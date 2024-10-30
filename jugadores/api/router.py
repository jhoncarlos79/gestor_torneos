from rest_framework.routers import DefaultRouter
from jugadores.api.views import JugadoreApiViewSet

router_jugadores = DefaultRouter()
router_jugadores.register(prefix='jugadores', basename='jugadores', viewset=JugadoreApiViewSet)