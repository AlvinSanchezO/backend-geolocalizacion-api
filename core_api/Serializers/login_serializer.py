# core_api/Serializers/login_serializer.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# IMPORTANTE: Importa tu modelo desde donde lo tengas (admin_geocesar o core_api)
from admin_geocesar.models import Empleado 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Obtenemos la validación original (los tokens access y refresh)
        data = super().validate(attrs)
        
        # BUSCAMOS EL NOMBRE REAL DEL EMPLEADO
        try:
            empleado_perfil = Empleado.objects.get(user=self.user)
            nombre_mostrar = empleado_perfil.nombre_completo
        except Empleado.DoesNotExist:
            # Si no tiene perfil, usamos su username como respaldo
            nombre_mostrar = self.user.username

        # AGREGAMOS LOS DATOS EXTRAS QUE EL FRONTEND NECESITA
        data['is_admin'] = self.user.is_staff
        data['username'] = self.user.username # Mantenemos el username por si acaso
        data['nombre_real'] = nombre_mostrar  # <--- ESTE ES EL NUEVO CAMPO
        data['user_id'] = self.user.id
        
        return data