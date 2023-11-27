#path es para poder poner rutas
from django.urls import path
from . import views
#este archivo es para gestionar las rutas solo de de esta app

urlpatterns = [
    #las views, vistas devuelvn una respuesta hacia el navegador y lo de entre '' es la referncia, apodo 
    # de la ruta del archivo,osea view. es una funcion con codigo que te retorna un archivo html
    #views.home accedes a la funcion home del archivo views, y te retorna el archivo html
   # path('',views.home), lo dentro de '' es la ruta por defecto que entra al correr la app
    path('', views.irLogin),
    path('comprobarLogin/', views.Login),
    path('irRegistro/', views.irRegistro),
    path('registrar/', views.Registrar),




]