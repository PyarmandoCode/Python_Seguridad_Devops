from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet,ArticulosListCreateAPIView

# router=DefaultRouter()
# router.register('articulos',ArticuloViewSet)

urlpatterns = [
    #path('',include(router.urls)),
    path('articuloslist/',ArticulosListCreateAPIView.as_view())
]
