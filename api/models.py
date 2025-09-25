from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    primerApellido = models.CharField(max_length=100)
    segundoApellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True) 
    numero_telefono = models.CharField(max_length=15, blank=True, null=True) 
    cargo = models.CharField(max_length=100)
    departamento=models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    horario = models.CharField(max_length=50, default='9:00 - 18:00')
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido}"