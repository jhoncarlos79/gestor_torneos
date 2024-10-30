from rest_framework.routers import DefaultRouter
from equipos.api.views import EquipoApiViewSet

router_equipos = DefaultRouter()
router_equipos.register(prefix='equipos', basename='equipos', viewset=EquipoApiViewSet)