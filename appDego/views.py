
from django.http import HttpResponse
from django.shortcuts import render
from appDego.models import *
from appDego.forms import Usuariosformulario
# Create your views here.

def inicio (request,):
    return render (request, 'appDego/index.html')

def usuarios (request):
    return render (request, 'appDego/usuarios.html')

def clientes (request):
    return render (request, 'appDego/clientes.html')

def impuestos (request):
    return render (request, 'appDego/impuestos.html')

def vencimientos (request):
    return render (request, 'appDego/vencimientos.html')

def foro (request):
    return render (request, 'appDego/foro.html')

def inicio_sesion (request):
    return render (request, 'appDego/inicio_sesion.html')

def formulario_usuario (request):

    if request.method == "POST":

        usuario = Usuariosformulario (request.POST)

        if usuario.is_valid(): 
            data = usuario.cleaned_data
            usuario_nuevo = Usuarios (data['nombre'], data['apellido'], data['documento'], data['email'])
            usuario_nuevo.save()
        
        return render (request, 'appDego/index.html')
    else:
        usuario_form = Usuariosformulario()
    return render (request, 'appDego/usuariosformulario.html',{'formulario': usuario_form} )

def buscar (request):
   
    if request.GET ['apellido']:
        apellido = request.GET['apellido']
        cliente = Clientes.objects.filter (apellido__icontains= apellido)
        return render (request, 'appDego/busquedacliente.html', { "apellido": apellido, 'cliente': cliente [0], 'cuit': cliente [0], 'email': cliente [0], 'telefono': cliente [0]})
    else:
        respuesta = "No se encontro el cliente"
    return HttpResponse (respuesta)


def buscar_cliente (request):
    return render (request, 'appDego/busquedacliente.html')
    
#     data = request.GET[['apellido']]
#     if data:
#         cliente = Clientes.objects.filter(apellido__icontains = data)
#         return render (request, 'appDego/busquedacliente.html', {"cliente": cliente, 'apellido': data})
#     return render (request, 'appDego/busquedacliente.html')

# def resultado (request):
#     respuesta = f''
'efrgrgtht'