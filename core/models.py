from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.ImageField(upload_to="productos/")

    def __str__(self):
        return self.nombre


class Detalle (models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    descripcion=models.TextField()
    stock= models.IntegerField
    color=models.CharField(max_length=50)
    fabricante=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.producto.nombre