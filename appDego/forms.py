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
    impuesto = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)
    codigo_impuesto = forms.IntegerField()
    repeticion = forms.CharField(max_length=40)

class Vencimientosformulario (forms.Form):
    impuesto = forms.CharField(max_length=40)
    codigo_impuesto = forms.IntegerField()
    fecha_vencimiento = forms.DateField()

class Foroformulario (forms.Form):
    usuario = forms.CharField(max_length=40)
    contraseña = forms.IntegerField()

