from rest_framework import serializers
from .models import ReservaCita, NotaCita
from clientes.serializers import ClienteSerializer
from profesional.serializers import ProfesionalSerializer

class ReservaCitaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    profesional = ProfesionalSerializer(read_only=True)

    class Meta:
        model = ReservaCita
        fields = ['id', 'cliente', 'profesional', 'fecha_cita', 'duracion', 'estado']

class NotaCitaSerializer(serializers.ModelSerializer):
    reserva_cita = ReservaCitaSerializer(read_only=True)

    class Meta:
        model = NotaCita
        fields = ['id', 'reserva_cita', 'nota', 'fecha_nota']
