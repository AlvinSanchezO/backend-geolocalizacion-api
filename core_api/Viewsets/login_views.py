# core_api/Viewsets/login_views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from core_api.Serializers.login_serializer import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer