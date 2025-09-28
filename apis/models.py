from django.db import models


class Articulos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.CharField(max_length=600)

    def __str__(self):
        return self.nombre
