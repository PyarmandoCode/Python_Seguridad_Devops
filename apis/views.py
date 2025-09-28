from rest_framework import viewsets
from .models import Articulos
from .serializers import ArticuloSerializer

"""
METODOS HTTP
============
GET .- lISTAR INFORMACION / OBTENER DETALLE
POST.-INSERTAR INFORMACION
PUT.-MODIFICAR INFORMACION
DELETE.-ELIMINAR INFORMACION
PATCH.-MODIFICAR INFORMACION
"""

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all()
    serializer_class = ArticuloSerializer


