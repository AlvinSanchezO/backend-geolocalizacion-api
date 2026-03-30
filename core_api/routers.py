from .Viewsets.empleado_viewset import EmpleadoViewSet
from .Viewsets.direccion_viewset import DireccionViewSet
from .Viewsets.monitoreo_views import MonitoreoViewSet 
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'empleados', EmpleadoViewSet)
router.register(r'direccion', DireccionViewSet)
router.register(r'monitoreo', MonitoreoViewSet, basename='monitoreo')