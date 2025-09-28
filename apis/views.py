from rest_framework import viewsets
from .models import Articulos
from .serializers import ArticuloSerializer

"""
UTILIZANDO APIVIEW
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

"""
METODOS HTTP
============
GET .- lISTAR INFORMACION / OBTENER DETALLE
POST.-INSERTAR INFORMACION
PUT.-MODIFICAR INFORMACION DEL OBJETO COMPLETO
DELETE.-ELIMINAR INFORMACION
PATCH.-MODIFICAR INFORMACION DE LOS CAMPOS QUE ENVIEES
"""

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all()
    serializer_class = ArticuloSerializer


class ArticulosListCreateAPIView(APIView):
    def get(self,request):
        articulos=Articulos.objects.all()
        serializer=ArticuloSerializer(articulos,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)