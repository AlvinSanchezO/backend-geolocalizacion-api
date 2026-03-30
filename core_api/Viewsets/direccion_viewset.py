from rest_framework import viewsets, permissions
from admin_geocesar.models import Direccion, Empleado
from core_api.Serializers.direccion_serializer import DireccionSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    
    # 1. SEGURIDAD: Solo usuarios logueados pueden mandar ubicación
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Este método se ejecuta JUSTO ANTES de guardar la ubicación.
        Busca al Empleado que está ligado al Usuario que mandó la petición.
        """
        # Obtenemos al usuario que mandó el POST (ej: Juan)
        usuario_actual = self.request.user
        
        try:
            # Buscamos el perfil de Empleado que le pertenece a ese Usuario
            empleado_perfil = Empleado.objects.get(user=usuario_actual)
            
            # Guardamos la dirección asignándole el empleado detectado automáticamente
            serializer.save(empleado=empleado_perfil)
            
            print(f"✅ Ubicación guardada exitosamente para: {empleado_perfil.nombre_completo}")
            
        except Empleado.DoesNotExist:
            # Si por alguna razón el usuario no tiene un perfil de Empleado creado
            print(f"❌ Error: El usuario {usuario_actual.username} no tiene un perfil de Empleado.")
            serializer.save()