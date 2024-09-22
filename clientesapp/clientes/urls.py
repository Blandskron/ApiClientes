from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ReservaViewSet, HistorialViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'historiales', HistorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
