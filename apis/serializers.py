from rest_framework import serializers
from .models import Articulos

class ArticuloSerializer (serializers.ModelSerializer):
    class Meta:
        model = Articulos
        fields = '__all__'