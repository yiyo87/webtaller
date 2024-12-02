from django.db import models


# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    numero = models.CharField(max_length=20)
    cantidad_bidones = models.PositiveIntegerField()

    def __str__(self):
        return f"Pedido de {self.nombre} ({self.cantidad_bidones} bidones)"