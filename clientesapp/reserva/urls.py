from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaCitaViewSet, NotaCitaViewSet

router = DefaultRouter()
router.register(r'reservas-citas', ReservaCitaViewSet)
router.register(r'notas-citas', NotaCitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
