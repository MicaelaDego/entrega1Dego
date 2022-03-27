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
    
