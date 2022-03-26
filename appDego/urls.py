from django.urls import path, URLPattern

from appDego.views import *

urlpatterns = [


path ('Usuarios/', usuarios),
path ('Clientes/', clientes),
path ('Impuestos/', impuestos),
path ('Vencimientos/', vencimientos),
path ('Foro/', foro),
path ('', inicio),


]