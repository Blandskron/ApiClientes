from rest_framework import serializers
from .models import Profesional, Area, Disponibilidad, Nota
from clientes.models import Cliente  # Importamos el modelo Cliente para las relaciones

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ['id', 'nombre', 'apellido', 'email', 'telefono', 'direccion']

class AreaSerializer(serializers.ModelSerializer):
    profesionales = ProfesionalSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ['id', 'nombre', 'descripcion', 'profesionales']

class DisponibilidadSerializer(serializers.ModelSerializer):
    profesional = ProfesionalSerializer(read_only=True)

    class Meta:
        model = Disponibilidad
        fields = ['id', 'profesional', 'dia_semana', 'hora_inicio', 'hora_fin']

class NotaSerializer(serializers.ModelSerializer):
    profesional = ProfesionalSerializer(read_only=True)
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())  # Para relacionar con cliente

    class Meta:
        model = Nota
        fields = ['id', 'profesional', 'cliente', 'nota', 'fecha_nota']
