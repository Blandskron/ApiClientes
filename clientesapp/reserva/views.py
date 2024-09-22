from rest_framework import viewsets
from .models import ReservaCita, NotaCita
from .serializers import ReservaCitaSerializer, NotaCitaSerializer

class ReservaCitaViewSet(viewsets.ModelViewSet):
    queryset = ReservaCita.objects.all()
    serializer_class = ReservaCitaSerializer

class NotaCitaViewSet(viewsets.ModelViewSet):
    queryset = NotaCita.objects.all()
    serializer_class = NotaCitaSerializer
