from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('api/',include('apis.urls'))
]

"""
GET
http://127.0.0.1:8000/api/articulos/
http://127.0.0.1:8000/api/articulos/1
POST
http://127.0.0.1:8000/api/articulos/
{
    "nombre": "SILLA GAMER",
    "precio": "900.00",
    "imagen": "https://res.cloudinary.com/dream-music/image/upload/v1626232246/album_10/gotcha_bq27pl.jpg"
}
PUT
http://127.0.0.1:8000/api/articulos/1/
{
    "nombre": "SILLA GAMER",
    "precio": "900.00",
    "imagen": "https://res.cloudinary.com/dream-music/image/upload/v1626232246/album_10/gotcha_bq27pl.jpg"
}
DELETE
http://127.0.0.1:8000/api/articulos/4/
"""