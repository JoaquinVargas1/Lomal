from django.shortcuts import render, redirect
from .models import Usuarios
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def irLogin(request):
        return render(request,'login.html')
    
def Login(request):
    
        # Para traer todos los objetos de TuModelo
        #objetos = Cursos.objects.all()

        # Para filtrar y traer objetos que cumplan cierta condición
        #objetos_filtrados = Cursos.objects.filter(campo1='ejemplo')

        # Puedes usar .get() para traer un objeto en específico
        #objeto_especifico = Cursos.objects.get(id=1)
        
        usuario=request.POST['txtUsuario']
        contrasenaPuesta=request.POST['txtContrasena']
        #objeto_especifico = Cursos.objects.get(id=1)
        try:
            usuario = Usuarios.objects.get(usuario=usuario, contrasena=contrasenaPuesta)
            print('igual')
            return render(request, 'tienda.html')
        except Usuarios.DoesNotExist:
            print('no igual')
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')            
            return render(request, 'login.html')
        
def irRegistro(request):
    return render(request,'registro.html')  
            
def Registrar(request):
    
       
        
        usuario=request.POST['txtUsuario']
        nombre=request.POST['txtNombre']
        apellido=request.POST['txtApellido']
        email=request.POST['txtEmail']
        contrasenaPuesta=request.POST['txtContrasena']
        
        nuevo_objeto = Usuarios(usuario=usuario, nombres=nombre,apellidos=apellido
                ,email=email,contrasena=contrasenaPuesta)
        nuevo_objeto.save()

        return redirect('/')