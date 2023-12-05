from django.shortcuts import render, redirect
from .models import Usuarios
from .models import Carrito
from .models import Sudaderas
from .models import Camisas
from .models import Tenis
from .models import Pantalones
from itertools import chain


from django.http import HttpResponse
from django.contrib import messages

from django.http import JsonResponse
from django.core.serializers import serialize

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
        
        usuarioTxt=request.POST['txtUsuario']
        contrasenaPuesta=request.POST['txtContrasena']
        #objeto_especifico = Cursos.objects.get(id=1)
        try:
            usuario = Usuarios.objects.get(usuario=usuarioTxt, contrasena=contrasenaPuesta)
            print('igual')
            
            return render(request, 'tienda.html',{'usuario':usuarioTxt})
    

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


    
def obtenerInformacionProductos(request,categoria,seccion):
    print('seccion '+categoria)
    
    #categoria es si es mujer nino o hombre y seccion si es pantalon, camisa etc..
    try:

        if(categoria=='inicio'):
           datosS = Sudaderas.objects.all()
           datosC = Camisas.objects.all()
           datosT = Tenis.objects.all()
           datosP = Pantalones.objects.all()

           datos = list(chain(datosC, datosP, datosS, datosT))
        else:
            match seccion:
                case 'camisa':
                    datos = Camisas.objects.filter(categoriaProducto=categoria)
                case 'sudadera':
                    datos = Sudaderas.objects.filter(categoriaProducto=categoria)
                case 'pantalon':
                    datos = Pantalones.objects.filter(categoriaProducto=categoria)
                case 'tenis':
                    datos = Tenis.objects.filter(categoriaProducto=categoria)
        
                    
        arreglo_datos = list(datos)
        arreglo_datos = serialize('json', datos, fields=('codigoProducto','nombreProducto', 'tallaProducto', 'precioProducto', 'imagenProducto','seccionProducto','categoriaProducto'))
        return JsonResponse({'data': arreglo_datos})

    except Sudaderas.DoesNotExist:
        print('No se encontraron datos')
        return JsonResponse({'error': 'No se encontraron datos con el código especificado'}, status=404)





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
@csrf_exempt 

@require_POST
def agregarProductoCarrito(request,usuario,codigo,seccion,categoria):
    print(seccion)
    usuarioDado = get_object_or_404(Usuarios, usuario=usuario)
    try:
        nuevo_objeto = Carrito(usuario=usuarioDado, codigo=codigo,seccion=seccion,categoria=categoria)
        nuevo_objeto.save()
        print('DATOS GUARDADOS CORRECTAMENTE')
        return JsonResponse({'message': 'Datos guardados correctamente'})
    except Exception as e:
        print('Error al guardar datos:', str(e))
        return JsonResponse({'error': 'Error al guardar datos'})
   
   
   

    
#cargamos todos los prouctos del carrito
def irCarrito(request, usuario):
    productos = Carrito.objects.filter(usuario=usuario)
    #cantidad  = Carrito.objects.filter(usuario=usuario).count()

   # print(cantidad)
    precioTotal=0
    listadosProductos = []  
    for producto in productos:
        if producto.seccion == 'camisa':
            listadosProductos += list(Camisas.objects.filter(codigoProducto=producto.codigo))
        elif producto.seccion == 'sudadera':
            listadosProductos += list(Sudaderas.objects.filter(codigoProducto=producto.codigo))
        elif producto.seccion == 'pantalon':
            listadosProductos += list(Pantalones.objects.filter(codigoProducto=producto.codigo))
        elif producto.seccion == 'teni':
            listadosProductos += list(Tenis.objects.filter(codigoProducto=producto.codigo))
        
    for precio in listadosProductos:
        precioTotal += precio.precioProducto
    
    #print(precioTotal)
    return render(request, 'carrito.html', {'productos': listadosProductos,'usuario': usuario,'precioTotal': precioTotal})


def borrarProductoCarrito(request, usuario, codigoProducto, seccionProducto):
    try:
        objeto_a_eliminar = Carrito.objects.filter(usuario=usuario, codigo=codigoProducto, seccion=seccionProducto).first()
        
        
        if objeto_a_eliminar:
            # Eliminar el objeto
            objeto_a_eliminar.delete()
            print('DATOS ELIMINADOS CORRECTAMENTE')
            return JsonResponse({'message': 'Datos ELIMINADOS correctamente'})
        else:
            print('No se encontraron datos para eliminar')
            return JsonResponse({'message': 'No se encontraron datos para eliminar'})
    except Exception as e:
        print('Error al ELIMINAR datos:', str(e))
        return JsonResponse({'error': 'Error al ELIMINAR datos'})
    
    
def actualizarCarrito(request, usuario):
    productos = Carrito.objects.filter(usuario=usuario)
    
    listadosProductos = []
    
    for producto in productos:
        queryset = Camisas.objects.none()  
        
        if producto.seccion == 'camisa':
            queryset = Camisas.objects.filter(codigoProducto=producto.codigo)
        elif producto.seccion == 'sudadera':
            queryset = Sudaderas.objects.filter(codigoProducto=producto.codigo)
        elif producto.seccion == 'pantalon':
            queryset = Pantalones.objects.filter(codigoProducto=producto.codigo)
        elif producto.seccion == 'teni':
            queryset = Tenis.objects.filter(codigoProducto=producto.codigo)
        
        if queryset.exists():
            listadosProductos.append(queryset.first())
   
    return render(request, 'carrito.html', {'productos': listadosProductos, 'usuario': usuario})



def irPerfil(request, usuario):
    datos = get_object_or_404(Usuarios, usuario=usuario)
    return render(request, 'perfil.html', {'usuario': usuario, 'datosUsuario': datos})


def actualizarDatos(request,usuario,nombre,apellido,email,contrasena):
    user = get_object_or_404(Usuarios, usuario=usuario)
    
    print(usuario)
    try:
        
        user.nombres = nombre
        user.apellidos = apellido
        user.email = email
        user.contrasena = contrasena
        user.save()
        return JsonResponse({ 'datos actualizados'})
    except  Exception as e:
        return JsonResponse({'error': 'Error al actualizar los datos'})

    


def eliminarCuenta(request,usuario):
    datos = get_object_or_404(Usuarios, usuario=usuario)
    
    try:
        
        datos.delete()
        return HttpResponse({'usuario borrado'})
    except  Exception as e:
        return HttpResponse({'error': 'Error al eliminar el usuario'})

