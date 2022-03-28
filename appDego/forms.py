from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from appDego.models import *

class Usuariosformulario (forms.Form):
    # campos del formulario
    nombre = forms.CharField (max_length=40)
    apellido = forms.CharField (max_length=40)
    documento = forms.IntegerField()
    email = forms.CharField(max_length=80)
    
class Clientesformulario (forms.Form):
    # campos del formulario
    nombre = forms.CharField (max_length=40)
    apellido = forms.CharField (max_length=40)
    cuit = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.CharField(max_length=80)
    
class Impuestosformulario (forms.Form):
    # campos del formulario
    impuesto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=40)
    codigo_impuesto = models.IntegerField()
    repeticion = models.CharField(max_length=40)

class Vencimientosformulario (forms.Form):
    impuesto = models.CharField(max_length=40)
    codigo_impuesto = models.IntegerField()
    fecha_vencimiento = models.DateField()