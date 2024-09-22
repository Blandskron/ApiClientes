from rest_framework import serializers
from .models import Cliente, Reserva, Historial

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'email', 'telefono', 'direccion']

class ReservaSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())

    class Meta:
        model = Reserva
        fields = ['id', 'cliente', 'fecha_reserva', 'fecha_llegada', 'fecha_salida', 'estado']

class HistorialSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())

    class Meta:
        model = Historial
        fields = ['id', 'cliente', 'actividad', 'fecha_actividad']
