from rest_framework.routers import DefaultRouter
from torneos.api.views import TorneoApiViewSet

router_torneos = DefaultRouter()
router_torneos.register(prefix='torneos', basename='torneos', viewset=TorneoApiViewSet)