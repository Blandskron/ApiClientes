from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfesionalViewSet, AreaViewSet, DisponibilidadViewSet, NotaViewSet

router = DefaultRouter()
router.register(r'profesionales', ProfesionalViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'disponibilidades', DisponibilidadViewSet)
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
