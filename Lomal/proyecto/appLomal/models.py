from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#rm -r appLomal/migrations
#python manage.py makemigrations --empty nombre_de_tu_app

# Create your models here.
class Usuarios(models.Model):
    usuario = models.CharField(max_length=100, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    contrasena= models.CharField(max_length=100)
    
    
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,to_field='usuario')
    codigo = models.IntegerField()
    seccion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)


 

#carrito funcionaria asi.. cuando se presione ir al carrito, ira a una funcion la cual
#buscara el producto mediante el codigo y los metera en un arreglo, retorna el arreglo 
#y en la funcionn pone su info del producto en el html del carrito pa que cuando entre
#esten los productos ahi        

#pip install Pillow

class Camisas(models.Model):
    
    OPCION_CAMISA = 'camisa'
    OPCION_PANTALON = 'pantalon'
    OPCION_SUDADERA = 'sudadera'
    OPCION_TENI = 'teni'
    
    OPCIONES_TIPO_PRENDA = [
        (OPCION_CAMISA, 'camisa'),
        (OPCION_PANTALON, 'pantalon'),
        (OPCION_SUDADERA, 'sudadera'),
        (OPCION_TENI, 'teni'),

    ]

    OPCION_HOMBRE = 'hombre'
    OPCION_MUJER = 'mujer'
    OPCION_NINO = 'nino'
    
    OPCIONES_GENERO = [
        (OPCION_HOMBRE, 'hombre'),
        (OPCION_MUJER, 'mujer'),
        (OPCION_NINO, 'nino'),

    ]
    
    OPCION_EXCH = 'EXCH'
    OPCION_CH = 'CH'
    OPCION_M = 'M'
    OPCION_G = 'G'
    OPCION_EXG = 'EXG'
    
    OPCIONES_TALLA = [
        (OPCION_EXCH, 'EXCH'),
        (OPCION_CH, 'CH'),
        (OPCION_M, 'M'),
        (OPCION_G, 'G'),
        (OPCION_EXG, 'EXG'),

    ]
    
    nombreProducto = models.CharField(max_length=100)
    codigoProducto = models.IntegerField(unique=True)
    tallaProducto = models.CharField(
        max_length=4,
        choices=OPCIONES_TALLA,
    )
    precioProducto = models.FloatField()
    imagenProducto = models.ImageField(upload_to='images/productos/Camisas')
    seccionProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_TIPO_PRENDA,
        default=OPCION_CAMISA 
    )
    categoriaProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_GENERO,
        default=OPCION_HOMBRE 
    )
    
    
class Sudaderas(models.Model):
    
    OPCION_CAMISA = 'camisa'
    OPCION_PANTALON = 'pantalon'
    OPCION_SUDADERA = 'sudadera'
    OPCION_TENI = 'teni'
    
    OPCIONES_TIPO_PRENDA = [
        (OPCION_CAMISA, 'camisa'),
        (OPCION_PANTALON, 'pantalon'),
        (OPCION_SUDADERA, 'sudadera'),
        (OPCION_TENI, 'teni'),

    ]

    OPCION_HOMBRE = 'hombre'
    OPCION_MUJER = 'mujer'
    OPCION_NINO = 'nino'
    
    OPCIONES_GENERO = [
        (OPCION_HOMBRE, 'hombre'),
        (OPCION_MUJER, 'mujer'),
        (OPCION_NINO, 'nino'),

    ]
    
    OPCION_EXCH = 'EXCH'
    OPCION_CH = 'CH'
    OPCION_M = 'M'
    OPCION_G = 'G'
    OPCION_EXG = 'EXG'
    
    OPCIONES_TALLA = [
        (OPCION_EXCH,'EXCH'),
        (OPCION_CH,'CH'),
        (OPCION_M,'M'),
        (OPCION_G,'G'),
        (OPCION_EXG,'EXG'),

    ]

    nombreProducto = models.CharField(max_length=100)
    codigoProducto = models.IntegerField(unique=True)
    tallaProducto = models.CharField(
        max_length=4,
        choices=OPCIONES_TALLA,
    )
    precioProducto = models.FloatField()
    imagenProducto = models.ImageField(upload_to='images/productos/Sudaderas')
    seccionProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_TIPO_PRENDA,
        default=OPCION_CAMISA 
    )
    categoriaProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_GENERO,
        default=OPCION_HOMBRE 
    )
    
class Pantalones(models.Model):
    
    OPCION_CAMISA = 'camisa'
    OPCION_PANTALON = 'pantalon'
    OPCION_SUDADERA = 'sudadera'
    OPCION_TENI = 'teni'
    
    OPCIONES_TIPO_PRENDA = [
        (OPCION_CAMISA, 'camisa'),
        (OPCION_PANTALON, 'pantalon'),
        (OPCION_SUDADERA, 'sudadera'),
        (OPCION_TENI, 'teni'),

    ]

    OPCION_HOMBRE = 'hombre'
    OPCION_MUJER = 'mujer'
    OPCION_NINO = 'nino'
    
    OPCIONES_GENERO = [
        (OPCION_HOMBRE, 'hombre'),
        (OPCION_MUJER, 'mujer'),
        (OPCION_NINO, 'nino'),

    ]

     
    OPCION_EXCH = 'EXCH'
    OPCION_CH = 'CH'
    OPCION_M = 'M'
    OPCION_G = 'G'
    OPCION_EXG = 'EXG'
    
    OPCIONES_TALLA = [
        (OPCION_EXCH,'EXCH'),
        (OPCION_CH,'CH'),
        (OPCION_M,'M'),
        (OPCION_G,'G'),
        (OPCION_EXG,'EXG'),

    ]
    
    nombreProducto = models.CharField(max_length=100)
    codigoProducto = models.IntegerField(unique=True)
    tallaProducto = models.CharField(
        max_length=4,
        choices=OPCIONES_TALLA,

    )
  
    precioProducto = models.FloatField()
    imagenProducto = models.ImageField(upload_to='images/productos/Pantalones')
    seccionProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_TIPO_PRENDA,
        default=OPCION_CAMISA 
    )
    categoriaProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_GENERO,
        default=OPCION_HOMBRE 
    )
    
class Tenis(models.Model):
    
    OPCION_CAMISA = 'camisa'
    OPCION_PANTALON = 'pantalon'
    OPCION_SUDADERA = 'sudadera'
    OPCION_TENI = 'teni'
    
    OPCIONES_TIPO_PRENDA = [
        (OPCION_CAMISA, 'camisa'),
        (OPCION_PANTALON, 'pantalon'),
        (OPCION_SUDADERA, 'sudadera'),
        (OPCION_TENI, 'teni'),

    ]

    OPCION_HOMBRE = 'hombre'
    OPCION_MUJER = 'mujer'
    OPCION_NINO = 'nino'
    
    OPCIONES_GENERO = [
        (OPCION_HOMBRE, 'hombre'),
        (OPCION_MUJER, 'mujer'),
        (OPCION_NINO, 'nino'),

    ]

    nombreProducto = models.CharField(max_length=100)
    codigoProducto = models.IntegerField(unique=True)
    tallaProducto = models.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(20)])
    precioProducto = models.FloatField()
    imagenProducto = models.ImageField(upload_to='images/productos/Tenis')
    seccionProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_TIPO_PRENDA,
        default=OPCION_CAMISA 
    )
    categoriaProducto = models.CharField(
        max_length=20,
        choices=OPCIONES_GENERO,
        default=OPCION_HOMBRE 
    )

  

    

