
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio (request):
    return HttpResponse('Vista de Inicio')

def usuarios (request):
    return HttpResponse ('vista de usuarios')

def clientes (request):
    return HttpResponse ('Vista de clientes')

def impuestos (request):
    return HttpResponse ('Vista de Impuestos')

def calendario_tareas (request):
    return HttpResponse ('Vista de tareas')

def foro (request):
    return HttpResponse ('Vista de Foro')