from django.shortcuts import render

from .models import Producto

def lista_productos(request):
    """
    ORM (OBJECT RELATION MAPPING)
    """
    productos=Producto.objects.all()
    return render (request,"index.html",{"productos":productos})


def detalle_producto(request):
    return render(request,"detalles.html")