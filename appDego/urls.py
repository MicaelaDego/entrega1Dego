from django.urls import path, URLPattern

from appDego.views import *

urlpatterns = [


path ('Usuarios/', usuarios, name= 'Usuarios'),
path ('Clientes/', clientes, name= 'Clientes' ),
path ('Impuestos/', impuestos, name = 'Impuestos'),
path ('Vencimientos/', vencimientos, name= 'Vencimientos'),
path ('Foro/', foro, name= 'Foro'),
path ('', inicio, name= 'Inicio' ),
path ('Inicio_sesion/', inicio_sesion, name = 'Inicio_sesion')


]