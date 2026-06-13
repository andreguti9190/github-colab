from django.urls import path
from .views import Home, Registro,VerProductos

urlpatterns = [
    path('', Home,name='home'),
    path('registro/', Registro,name='registro'),
    path('productos/', VerProductos,name='productos'),
]
