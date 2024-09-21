from django.db import models
from clientes.models import Cliente  # Importamos el modelo Cliente de la otra app

class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesionales = models.ManyToManyField(Profesional, related_name='areas')

    def __str__(self):
        return self.nombre

class Disponibilidad(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='disponibilidades')
    dia_semana = models.CharField(max_length=10, choices=[
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo')
    ])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.profesional.nombre} disponible el {self.dia_semana} de {self.hora_inicio} a {self.hora_fin}"

class Nota(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='notas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cliente viene del otro app
    nota = models.TextField()
    fecha_nota = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota de {self.profesional.nombre} para {self.cliente.nombre}: {self.fecha_nota}"
