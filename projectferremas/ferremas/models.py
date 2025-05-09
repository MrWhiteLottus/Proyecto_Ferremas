from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(max_length=10)
    fecha_compra = models.DateField()

    def __str__(self):
        return self.nombre
