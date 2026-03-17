from .Viewsets.empleado_viewset import EmpleadoViewSet
from .Viewsets.direccion_viewset import DireccionViewSet
from rest_framework import routers

# Cambiamos el nombre de la variable a 'router' (singular)
router = routers.DefaultRouter()

# Registramos usando la nueva variable 'router'
router.register(r'empleados', EmpleadoViewSet)
router.register(r'direccion', DireccionViewSet)