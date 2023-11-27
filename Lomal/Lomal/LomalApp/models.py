from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usuario = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    contrasena= models.CharField(max_length=100)