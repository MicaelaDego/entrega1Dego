
from django.http import HttpResponse
from django.shortcuts import render

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