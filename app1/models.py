from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre_cliente = models.CharField(max_length=15, default="")
    apellido = models.CharField(max_length=15,  default="")
    email = models.EmailField(default="")

class fondos(models.Model):
    nombre_fondo=models.CharField(max_length=30)
    cant_activos=models.IntegerField()


class bonos (models.Model):
    nombre_bonos=models.CharField(max_length=30)
    ticket= models.CharField(max_length=6)
    valor_nominal=models.IntegerField()
    valor_mercado=models.IntegerField()
    tir=models.IntegerField()

class acciones (models.Model):
    nombre_acciones=models.CharField(max_length=30)
    ticket= models.CharField(max_length=6)
    precio=models.IntegerField()

