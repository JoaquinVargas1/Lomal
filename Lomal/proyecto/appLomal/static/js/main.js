// el function indica que el codigo de dentro se va a esperar a que la pagina este cargada 
//antes de ejecutar el codigo
(function (){
    var seccion = 'camisa'
    var categoria = 'hombre'

    

    $.ajax({
               
        url: '/obtenerInformacionProductos/inicio/' + seccion + '/',
        method: 'GET',
        success: function(data) {

            actualizarDoom(data)
        },
        error: function(error) {
            console.error('Error al obtener información:', error);
        }
    });


    //listener al boton para ir al carrito
    var btnIrCarrito = document.getElementById("btnIrCarrito");
    btnIrCarrito.addEventListener("click", function() {
        usuario = document.getElementById("usuario").innerHTML;

        $.ajax({
            url: '/irCarrito/' + usuario + '/',
            method: 'GET',
            success: function(data) {
                console.log('todo clean');  
                window.location.href = '/irCarrito/' + usuario + '/';

            },
            error: function(error) {
                console.error('Error al obtener información:', error);
            }
        });
    });



     //listeners a los menus 
    $(document).ready(function() {
        // Manejar clics en el primer menú
        $('#menu1 a').on('click', function(e) {
            e.preventDefault();
            categoria = $(this).data('section');

            $.ajax({
                url: '/obtenerInformacionProductos/' + categoria + '/' + seccion + '/',
                method: 'GET',

                success: function(data) {
                    // Verifica si 'data' está presente en la respuesta
                    if (data.data) {
                        actualizarDoom(data);
                
                    } else {
                        console.error('El campo "data" está ausente en la respuesta.');
                    }
                },
                error: function(error) {
                    console.error('Error al obtener información:', error);
                }
            });
            
            
        });
    
         //Manejar clics en el segundo menú
        $('#menu2 a').on('click', function(e) {
            e.preventDefault();
            seccion = $(this).data('category');

            if(categoria=='inicio'){
                categoria='hombre'
            }
            $.ajax({
               
                url: '/obtenerInformacionProductos/' + categoria + '/' + seccion + '/',
                method: 'GET',
                success: function(data) {

                    actualizarDoom(data)
                },
                error: function(error) {
                    console.error('Error al obtener información:', error);
                }
            });
        });
    });
})();



function actualizarDoom(data) {
    // Eliminar elementos con el id "container"
    var container = document.getElementById("productos");
    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }
  
    var datos_deserializados = JSON.parse(data.data);
    var STATIC_URL = '/static/';
  
    var productosContainer = document.getElementById("productos");
    productosContainer.id = "productos";
    
    for (let i = 0; i < datos_deserializados.length; i++) {
      // Crea una nueva etiqueta div para cada producto
      var div = document.createElement("div");
      div.className = "producto " + i;
    
      var imagenHTML = '<img id="imagenProducto_'+i+'" src="' + STATIC_URL + datos_deserializados[i].fields.imagenProducto + '" alt="No encontrado">';
      var nombreHTML = '<p id="nombreProducto_'+i+'">' + datos_deserializados[i].fields.nombreProducto + '</p>';
      var tallaHTML = '<p id="tallaProducto_'+i+'">Talla: ' + datos_deserializados[i].fields.tallaProducto + '</p>';
      var codigoHTML = '<p id="codigoProducto_' + i + '" data-codigo="' + datos_deserializados[i].fields.codigoProducto + '" data-seccion="'+ datos_deserializados[i].fields.seccionProducto + '" data-categoria="'+ 
      datos_deserializados[i].fields.categoriaProducto + '">Código: ' + datos_deserializados[i].fields.codigoProducto + '</p>';
      var precioHTML = '<p id="precioProducto_'+i+'">Precio: ' + datos_deserializados[i].fields.precioProducto+ '</p>';
      var btnAgregarCarrtio = '<button id="btn_producto_'+i+'">Agregar al carrito</button>';
    
      // Concatenar las etiquetas antes de asignarlas a innerHTML
      div.innerHTML += imagenHTML + nombreHTML + tallaHTML + codigoHTML + precioHTML + btnAgregarCarrtio;
    
      // Agregar cada contenedor de producto al contenedor principal
      productosContainer.appendChild(div);
    
      // Agregar productos al carrito  --------
      var btn = document.getElementById("btn_producto_" + i);
    
      btn.addEventListener("click", (function(index) {
        return function(event) {

            var usuario = document.getElementById("usuario").innerText;
            var codigo = document.getElementById("codigoProducto_" + i).getAttribute("data-codigo");
            var seccion_ = document.getElementById("codigoProducto_" + i).getAttribute("data-seccion");
            var categoria = document.getElementById("codigoProducto_" + i).getAttribute("data-categoria");
           
       
        $.ajax({
            url: '/agregarProductoCarrito/' + usuario + '/' + codigo + '/'+ seccion_ +'/' + categoria + '/',
            method: 'POST',

            success: function(data) {
                console.log(" todo bien")

            },
            error: function(error) {
                console.error('Error al obtener información:', error);
            }
        });
          
          console.log("Botón clickeado para el producto " + index);
        };
      })(i));
    }
    
    // Agregar el contenedor principal al cuerpo del documento
    document.body.appendChild(productosContainer);
}
  

function irPerfil(){
    var usuario = document.getElementById("usuario").innerText
    //voy a la vista django que me envia al archivo perfil.html
    window.location.href = '/irPerfil/'+usuario+'/';
}