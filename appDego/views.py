
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

def vencimientos (request):
    return render (request, 'appDego/vencimientos.html')

def foro (request):
    return render (request, 'appDego/foro.html')



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

# buscar datos cliente 
def buscar (request):
   
    if request.GET ['apellido']:
        apellido = request.GET['apellido']
        cliente = Clientes.objects.filter (apellido__icontains= apellido)
        return render (request, 'appDego/busquedacliente.html', { "apellido": apellido, 'cliente': cliente [0], 'cuit': cliente [0], 'email': cliente [0], 'telefono': cliente [0]})
    else:
        respuesta = "No se encontro el cliente"
    return HttpResponse (respuesta)

# cargar datos cliente     
def formulario_cliente (request):

    if request.method == "POST":

        cliente = Clientesformulario (request.POST)

        if cliente.is_valid(): 
            data = cliente.cleaned_data
            cliente_nuevo = Clientes (data['nombre'], data ['apellido'], data ['cuit'],  data ['telefono'], data['email'])
            cliente_nuevo.save()
        
        return render (request, 'appDego/index.html')
    else:
        cliente_form = Clientesformulario()
    return render (request, 'appDego/clientesformulario.html',{'formulario': cliente_form} )

def formulario_impuestos (request):

    if request.method == "POST":

        impuesto = Impuestosformulario (request.POST)

        if impuesto.is_valid(): 
            data = impuesto.cleaned_data
            impuesto_nuevo = Impuestos (data['impuesto'], data ['tipo'], data ['codigo_impuesto'],  data ['repeticion'])
            impuesto_nuevo.save()
        
        return render (request, 'appDego/index.html')
    else:
        impuestos_form = Impuestosformulario()
    return render (request, 'appDego/impuestosformulario.html',{'formulario': impuestos_form} )

def formulario_vencimientos (request):

    if request.method == "POST":

        vencimiento = Vencimientosformulario (request.POST)

        if vencimiento.is_valid(): 
            data = vencimiento.cleaned_data
            vencimiento_nuevo = Impuestos (data['impuesto'], data ['codigo_impuesto'], data ['fecha_vencimiento'])
            vencimiento_nuevo.save()
        
        return render (request, 'appDego/index.html')
    else:
        vencimientos_form = Vencimientosformulario()
    return render (request, 'appDego/vencimientosformulario.html',{'formulario': vencimientos_form} )

