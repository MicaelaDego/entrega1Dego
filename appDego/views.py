

from sqlite3 import apilevel
from django.http import HttpResponse
from django.shortcuts import render
from appDego.models import *
from appDego.forms import *
# Create your views here.

def inicio (request,):
    return render (request, 'appDego/index.html')

def usuarios (request):
    usuario = Usuarios.objects.all()
    if request.method == "POST":
        usuario = Usuariosformulario (request.POST)

        if usuario.is_valid(): 
            data = usuario.cleaned_data
            usuario_nuevo = Usuarios (data['nombre'], data['apellido'], data['documento'], data['email'])
            usuario_nuevo.save()
            formulario = Clientesformulario()
            return render (request, 'appDego/usuarios.html', {'usuario': usuario, 'title' : 'Usuarios', 'page':'Usuarios', 'formulario': formulario})

    else:
        formulario = Usuariosformulario()
        return render (request, 'appDego/usuarios.html', {'usuario': usuario, 'title' : 'Usuarios', 'page':'Usuarios', 'formulario': formulario})

    return render (request, 'appDego/usuarios.html')

def clientes (request):
    cliente = Clientes.objects.all()

    if request.method == 'POST':
        cliente = Clientesformulario (request.POST)

        if cliente.is_valid(): 
            data = cliente.cleaned_data
            cliente_nuevo = Clientes (data['nombre'], data['apellido'], data['cuit'], data['telefono'], data ['email'])
            cliente_nuevo.save()
            formulario = Clientesformulario()
            return render (request, 'appDego/clientes.html', {'cliente': cliente, 'title' : 'Clientes', 'page':'Clientes', 'formulario': formulario})

    else:
        formulario = Clientesformulario()
        return render (request, 'appDego/clientes.html', {'cliente': cliente, 'title' : 'Clientes', 'page':'Clientes', 'formulario': formulario})
    
       




def impuestos (request):
    impuesto = Impuestos.objects.all()
    if request.method == "POST":
        impuesto = Impuestosformulario (request.POST)
        if impuesto.is_valid(): 
            data = impuesto.cleaned_data
            impuesto_nuevo = Impuestos (data['impuesto'], data['tipo'], data['codigo_impuesto'], data['repeticion'])
            impuesto_nuevo.save()
            formulario = Impuestosformulario()
            return render (request, 'appDego/impuestos.html', {'impuesto': impuesto, 'title' : 'Impuestos', 'page':'Impuestos', 'formulario': formulario})
         
    else:
        formulario = Impuestosformulario()
        return render (request, 'appDego/impuestos.html', {'impuesto': impuesto, 'title' : 'Impuestos', 'page':'Impuestos', 'formulario': formulario})
  
    

def foro (request):
    return render (request, 'appDego/foro.html')



# formulario para cargar usuarios

# def formulario_usuario (request):

#     if request.method == "POST":

#         usuario = Usuariosformulario (request.POST)

#         if usuario.is_valid(): 
#             data = usuario.cleaned_data
#             usuario_nuevo = Usuarios (data['nombre'], data['apellido'], data['documento'], data['email'])
#             usuario_nuevo.save()
        
#         return render (request, 'appDego/index.html')
#     else:
#         usuario_form = Usuariosformulario()
#     return render (request, 'appDego/usuariosformulario.html',{'formulario': usuario_form} )

# formulario para cargar clientes

# def formulario_cliente (request):

#     if request.method == "POST":

#         cliente = Clientesformulario (request.POST)

#         if cliente.is_valid(): 
#             data = cliente.cleaned_data
#             cliente_nuevo = Clientes (data['nombre'], data['apellido'], data['cuit'], data['telefono'], data ['email'])
#             cliente_nuevo.save()
        
#         return render (request, 'appDego/index.html')
#     else:
#         usuario_form = Clientesformulario ()
#     return render (request, 'appDego/clientesformulario.html',{'formulario': usuario_form} )


# formulario para cargae impuestos 

# def formulario_impuesto (request):

#     if request.method == "POST":

#         impuesto = Impuestosformulario (request.POST)

#         if impuesto.is_valid(): 
#             data = impuesto.cleaned_data
#             impuesto_nuevo = Impuestos (data['impuesto'], data['tipo'], data['codigo_impuesto'], data['repeticion'])
#             impuesto_nuevo.save()
        
#         return render (request, 'appDego/index.html')
#     else:
#         usuario_form = Impuestosformulario()
#     return render (request, 'appDego/impuestosformulario.html',{'formulario': usuario_form} )


# formulario para crear usuario y contraseña

# def formulario_foro (request):

#     if request.method == "POST":

#         usuario = Foroformulario (request.POST)

#         if usuario.is_valid(): 
#             data = usuario.cleaned_data
#             usuario_nuevo = Foro (data['usuario'], data['contraseña'])
#             usuario_nuevo.save()
        
#         return render (request, 'appDego/foro.html')
#     else:
#         usuario_form = Foroformulario()
#     return render (request, 'appDego/foroformulario.html',{'formulario': usuario_form} )

def buscar (request):
    apellido = request.GET['apellido'] 
    try: 
        if apellido:
        
            cliente = Clientes.objects.filter (apellido__icontains= apellido)
        
            return render (request, 'appDego/buscarcliente.html', { "apellido": apellido, 'cliente': cliente[0]})
        return render (request, 'appDego/buscarcliente.html')

    except: 
        return render (request,'appDego/buscarcliente.html' )

def buscar_cliente (request):
    return render (request, 'appDego/buscarcliente.html')

