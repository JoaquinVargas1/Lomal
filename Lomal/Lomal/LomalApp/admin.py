from django.contrib import admin
from .models import Usuarios

# Register your models here.
#esto es para registrar mis modelos en el panel administrador del super usuario
admin.site.register(Usuarios)
