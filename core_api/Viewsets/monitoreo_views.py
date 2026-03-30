# core_api/Viewsets/monitoreo_views.py
from rest_framework import viewsets, permissions
from admin_geocesar.models import Empleado, Direccion
from ..Serializers.monitoreo_serializer import MonitoreoSerializer

class MonitoreoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Vista protegida: Permite al Administrador ver la lista de todos 
    los empleados y su última ubicación GPS registrada.
    """
    # 1. Traemos a todos los empleados de la base de datos
    queryset = Empleado.objects.all()
    
    # 2. Usamos el serializer que creamos anteriormente
    serializer_class = MonitoreoSerializer
    
    # 3. SEGURIDAD: Solo usuarios con "Staff Status" en Django pueden entrar
    # Si un empleado normal intenta entrar, recibirá un error 403 Forbidden
    permission_classes = [permissions.IsAdminUser]