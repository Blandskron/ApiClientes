from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField()
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ])

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} para el {self.fecha_llegada}"

class Historial(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='historial')
    actividad = models.CharField(max_length=255)
    fecha_actividad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historial de {self.cliente.nombre}: {self.actividad}"
