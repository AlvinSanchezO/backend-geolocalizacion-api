# core_api/Serializers/monitoreo_serializer.py
from rest_framework import serializers
from admin_geocesar.models import Empleado, Direccion

class MonitoreoSerializer(serializers.ModelSerializer):
    # Campo calculado para traer la información de la última ubicación
    ultima_ubicacion = serializers.SerializerMethodField()

    class Meta:
        model = Empleado
        fields = ['id', 'nombre_completo', 'puesto', 'ultima_ubicacion']

    def get_ultima_ubicacion(self, obj):
        # Buscamos la dirección más reciente registrada por este empleado
        # Usamos 'fecha_registro' para ordenar de la más nueva a la más vieja
        ultima = Direccion.objects.filter(empleado=obj).order_by('-fecha_registro').first()
        
        if ultima:
            return {
                "latitud": ultima.latitud,
                "longitud": ultima.longitud,
                "direccion_texto": ultima.direccion_completa, # ¡Aprovechamos tu función!
                "fecha": ultima.fecha_registro.strftime("%d/%m/%Y %H:%M") # Formato legible
            }
        return None