from django.urls import path
from .views import Home, Registro

urlpatterns = [
    path('', Home,name='home'),
    path('registro/', Registro,name='registro'),
]
