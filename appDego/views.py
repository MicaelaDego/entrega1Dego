

from django.http import HttpResponse
from django.shortcuts import render
from appDego.models import *
from appDego.forms import *
# Create your views here.

def inicio (request,):
    return render (request, 'appDego/index.html')

def usuarios (request):
    return render (request, 'appDego/usuarios.html')

def clientes (request):
    return render (request, 'appDego/clientes.html')

def impuestos (request):
    return render (request, 'appDego/impuestos.html')


def foro (request):
    return render (request, 'appDego/foro.html')



# formulario para cargar usuarios

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

# formulario para cargar clientes

def formulario_cliente (request):

    if request.method == "POST":

        cliente = Clientesformulario (request.POST)

        if cliente.is_valid(): 
            data = cliente.cleaned_data
            cliente_nuevo = Clientes (data['nombre'], data['apellido'], data['cuit'], data['telefono'], data ['email'])
            cliente_nuevo.save()
        
        return render (request, 'appDego/index.html')
    else:
        usuario_form = Clientesformulario ()
    return render (request, 'appDego/clientesformulario.html',{'formulario': usuario_form} )

# formulario para cargae impuestos 

def formulario_impuesto (request):

    if request.method == "POST":

        impuesto = Impuestosformulario (request.POST)

        if impuesto.is_valid(): 
            data = impuesto.cleaned_data
            impuesto_nuevo = Impuestos (data['impuesto'], data['tipo'], data['codigo_impuesto'], data['repeticion'])
            impuesto_nuevo.save()
        
        return render (request, 'appDego/index.html')
    else:
        usuario_form = Impuestosformulario()
    return render (request, 'appDego/impuestosformulario.html',{'formulario': usuario_form} )


# formulario para crear usuario y contraseña

def formulario_foro (request):

    if request.method == "POST":

        usuario = Foroformulario (request.POST)

        if usuario.is_valid(): 
            data = usuario.cleaned_data
            usuario_nuevo = Foro (data['usuario'], data['contraseña'])
            usuario_nuevo.save()
        
        return render (request, 'appDego/foro.html')
    else:
        usuario_form = Foroformulario()
    return render (request, 'appDego/foroformulario.html',{'formulario': usuario_form} )


# def buscar (request):

   
#     if request.GET ['apellido']:
        
#         apellido = request.GET['apellido']
#         cliente = Clientes.objects.filter (apellido__icontains= apellido)
#         return render (request, 'appDego/buscarcliente.html', { "apellido": apellido, 'cliente': cliente [0], 'cuit': cliente [0], 'email': cliente [0], 'telefono': cliente [0]})
#     else:
#         respuesta = "No se encontro el cliente"
#     return HttpResponse (respuesta)

# def buscar_cliente (request):
#     return render (request, 'appDego/busquedacliente.html')
    
