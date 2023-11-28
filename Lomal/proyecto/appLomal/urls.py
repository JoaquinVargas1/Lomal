from django.urls import path
from django.conf import settings
from .views import irLogin, Login, irCarrito, irRegistro, Registrar, obtenerInformacionProductos,agregarProductoCarrito,borrarProductoCarrito,actualizarCarrito,irPerfil
from django.conf.urls.static import static

urlpatterns = [
    #las views, vistas devuelvn una respuesta hacia el navegador y lo de entre '' es la referncia, apodo 
    # de la ruta del archivo,osea view. es una funcion con codigo que te retorna un archivo html
    #views.home accedes a la funcion home del archivo views, y te retorna el archivo html
   # path('',views.home), lo dentro de '' es la ruta por defecto que entra al correr la app
    path('', irLogin),
    path('comprobarLogin/', Login),
    path('irRegistro/', irRegistro),
    path('registrar/', Registrar),
    path('irCarrito/<str:usuario>/', irCarrito),
    #path('obtenerInformacionProductos/<str:section>/', obtenerInformacionProductos, name='obtener_informacion_productos'),
    path('obtenerInformacionProductos/<str:categoria>/<str:seccion>/', obtenerInformacionProductos),
    path('agregarProductoCarrito/<str:usuario>/<str:codigo>/<str:seccion>/<str:categoria>/', agregarProductoCarrito),
    path('borrarProductoCarrito/<str:usuario>/<str:codigoProducto>/<str:seccionProducto>/', borrarProductoCarrito),
    path('actualizarCarrito/<str:usuario>/', actualizarCarrito),
    path('irPerfil/<str:usuario>/', irPerfil),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
