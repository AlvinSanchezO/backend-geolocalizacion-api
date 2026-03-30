from django.urls import path, include
from .routers import router
from .Viewsets.login_views import MyTokenObtainPairView

urlpatterns = [
    # 2. Ruta para el Login con el Serializer que dice si es Admin
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Rutas de modelos (empleados, direcciones, etc.)
    path('api-cesar/', include(router.urls)),
]