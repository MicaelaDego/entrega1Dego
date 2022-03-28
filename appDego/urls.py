from django.urls import path, URLPattern

from appDego.views import *

urlpatterns = [


path ('Usuarios/', usuarios, name= 'Usuarios'),
path ('Clientes/', clientes, name= 'Clientes' ),
path ('Impuestos/', impuestos, name = 'Impuestos'),
path ('Foro/', foro, name= 'Foro'),
path ('', inicio, name= 'Inicio' ),
path ('usuariosformulario/', formulario_usuario, name = 'usuariosformulario'),
path ('clientesformulario/', formulario_cliente, name = 'clientesformulario'),
path ('impuestosformulario/', formulario_impuesto, name = 'impuestosformulario'),
path ('foroformulario/', formulario_foro, name= 'foroformulario')



]