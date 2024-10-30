from rest_framework.routers import DefaultRouter
from deportes.api.views import DeporteApiViewSet

router_deportes = DefaultRouter()
router_deportes.register(prefix='deportes', basename='deportes', viewset=DeporteApiViewSet)