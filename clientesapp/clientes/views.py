from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente, Reserva, Historial
from .serializers import ClienteSerializer, ReservaSerializer, HistorialSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def retrieve(self, request, pk=None):
        """
        Sobrescribe el método retrieve para personalizar la respuesta al obtener un cliente por su pk.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
