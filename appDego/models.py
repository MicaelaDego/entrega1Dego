from django.db import models

# Create your models here.

class Usuarios (models.Model):
    nombre = models.CharField(max_length= 40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField(primary_key=True)
    mail = models.EmailField()

class Clientes (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cuit=models.IntegerField(primary_key=True)
    telefono = models.IntegerField()
    email = models.EmailField()
    

class Impuestos (models.Model):
    impuesto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=40)
    codigo_impuesto = models.IntegerField(primary_key=True)
    repeticion = models.CharField(max_length=40)

class Calendario_Tareas (models.Model):
    impuesto = models.CharField(max_length=40)
    codigo_impuesto = models.IntegerField()
    fecha_vencimiento = models.DateField()

class Foro(models.Model):
    usuario = models.CharField(max_length=40)
    contraseña = models.IntegerField()
