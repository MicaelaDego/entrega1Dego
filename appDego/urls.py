from django.urls import path, URLPattern

from appDego.views import *

urlpatterns = [


path ('Usuarios/', usuarios),
path ('Clientes/', clientes),
path ('Impuestos/', impuestos),
path ('Tareas/', calendario_tareas),
path ('Foro/', foro),
path ('', inicio),


]