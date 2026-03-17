from django.urls import path, include
from .routers import router

urlpatterns = [
    # Usamos router.urls (en singular, igual que en la importación de arriba)
    path('api-cesar/', include(router.urls)),
]