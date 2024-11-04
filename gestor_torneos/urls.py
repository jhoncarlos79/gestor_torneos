"""
URL configuration for gestor_torneos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Rutas propias
from deportes.api.router import router_deportes
from equipos.api.router import router_equipos
from inscripciones.api.router import router_inscripciones
from jugadores.api.router import router_jugadores
from partidos.api.router import router_partidos
#from resultados.api.router import router_resultados
from torneos.api.router import router_torneos

schema_view = get_schema_view(
   openapi.Info(
      title="Gestor de Torneos",
      default_version='v1',
      description="Documentacion API del Proyecto Gestor Torneos",
      terms_of_service="",
      contact=openapi.Contact(email="jhoncarlos@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api', include('users.api.router')),
    path('api', include(router_deportes.urls)),
    path('api', include(router_equipos.urls)),
    path('api', include(router_inscripciones.urls)),
    path('api', include(router_jugadores.urls)),
    path('api', include(router_partidos.urls)),
    #path('api', include(router_resultados.urls)),
    path('api', include(router_torneos.urls))   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header='ADMINISTRADOR GESTOR DE TORNEOS'