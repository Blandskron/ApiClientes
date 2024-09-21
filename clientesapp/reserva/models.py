from django.db import models
from clientes.models import Cliente  # Importamos el modelo Cliente de la otra app
from profesional.models import Profesional  # Importamos el modelo Profesional de la app de profesionales

class ReservaCita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas_citas')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='reservas_citas')
    fecha_cita = models.DateTimeField()
    duracion = models.DurationField(help_text="Duración de la cita (HH:MM:SS)")
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ])

    def __str__(self):
        return f"Cita de {self.cliente.nombre} con {self.profesional.nombre} el {self.fecha_cita}"

class NotaCita(models.Model):
    reserva_cita = models.ForeignKey(ReservaCita, on_delete=models.CASCADE, related_name='notas')
    nota = models.TextField()
    fecha_nota = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota de la cita: {self.reserva_cita.cliente.nombre} con {self.reserva_cita.profesional.nombre} en {self.reserva_cita.fecha_cita}"
