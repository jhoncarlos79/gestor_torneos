from rest_framework.routers import DefaultRouter
from inscripciones.api.views import IncripcioneApiViewSet

router_inscripciones = DefaultRouter()
router_inscripciones.register(prefix='inscripciones', basename='inscripciones', viewset=IncripcioneApiViewSet)