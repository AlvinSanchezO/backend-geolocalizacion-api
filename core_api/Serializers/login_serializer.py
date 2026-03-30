# core_api/Serializers/login_serializer.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Obtenemos la validación original (los tokens access y refresh)
        data = super().validate(attrs)
        
        # AGREGAMOS LOS DATOS EXTRAS QUE EL FRONTEND NECESITA
        data['is_admin'] = self.user.is_staff  # True si es de CESUN/Admin
        data['username'] = self.user.username
        data['user_id'] = self.user.id
        
        return data