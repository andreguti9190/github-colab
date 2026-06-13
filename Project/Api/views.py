from django.shortcuts import render
from .forms import *

# Create your views here.
def Home(request):
    return render(request,'Base.html')

def Registro(request):
    data={}
    data['formulario']=FormularioRegistro()
    if request.method=="POST":
        query=FormularioRegistro(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data["mensaje"]="Datos Registrados"
        else:
            data['mensaje']="No se pudo Registrados"
    return render(request,'pages/Registro.html',data)

def VerProductos(request):
    query=Alumnos.objects.all()
    data={}
    data['productos']=query
    return render(request,'pages/Productos.html',data)