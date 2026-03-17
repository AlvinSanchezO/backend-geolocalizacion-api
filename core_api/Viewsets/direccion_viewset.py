from rest_framework import viewsets

from admin_geocesar.models import Direccion 

from core_api.Serializers.direccion_serializer import DireccionSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer