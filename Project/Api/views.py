from django.shortcuts import render
from .forms import *

# Create your views here.
def Home(request):
    return render(request,'Base.html')

def Registro(request):
    data={}
    data['formulario']=FormularioRegistro()
    return render(request,'pages/Registro.html',data)
