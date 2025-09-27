from django.urls import path
from .views import lista_productos,detalle_producto

urlpatterns = [
    path('', lista_productos),
    path('detalles/', detalle_producto),
]