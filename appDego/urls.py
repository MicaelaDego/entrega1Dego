from django.urls import path, URLPattern

from appDego.views import *

urlpatterns = [


path ('Usuarios/', usuarios, name= 'Usuarios'),
path ('Clientes/', clientes, name= 'Clientes' ),
path ('Impuestos/', impuestos, name = 'Impuestos'),
path ('Vencimientos/', vencimientos, name= 'Vencimientos'),
path ('Foro/', foro, name= 'Foro'),
path ('', inicio, name= 'Inicio' ),

path ('usuariosformulario/', formulario_usuario, name = 'usuariosformulario'),
path ('clientesformulario/', formulario_cliente , name  = 'clientesformulario'),
path ('impuestosformulario/', formulario_impuestos , name = 'impuestosformulario'),
path ('vencimientosformulario/', formulario_vencimientos, name = 'vencimientosformualrio'),
path ('busquedacliente/', buscar, name = 'busquedacliente'),
path ('buscar/', buscar)


]