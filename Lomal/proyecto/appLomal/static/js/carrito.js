function eliminarProducto(codigoProducto, seccionProducto) {
    usuario = document.getElementById("nombreUsuario").getAttribute("data-nombreUsuario");

    // Llamamos a la vista borrarProductoCarrito
    $.ajax({
        url: '/borrarProductoCarrito/' + usuario + '/' + codigoProducto + '/' + seccionProducto + '/',
        method: 'GET',
        success: function () {
            console.log('Producto borrado');

           
            // Llamamos a la vista irCarrito para actualizar el carrito
            $.ajax({
                url: '/actualizarCarrito/' + usuario + '/',
                method: 'GET',
                success: function (response) {
                    console.log('Carrito actualizado');
                    
                    // Actualizamos el contenido HTML con el nuevo carrito
                    $('body').html(response);

                    //calculamos el precio total
                    calcularPrecio()

                },
                error: function (error) {
                    console.error('Error al actualizar información:', error);
                }
            });
        },
        error: function (error) {
            console.error('Error al borrar el producto:', error);
        }
    });
}


function calcularPrecio(){
    var tablaCarrito = document.getElementById("tablaCarrito");

    var filas = tablaCarrito.getElementsByTagName("tr");

    var sumaPrecios = 0;

    // Iterar sobre cada fila (comenzando desde la segunda fila, ya que la primera es el encabezado)
    for (var i = 1; i < filas.length; i++) {
        // Obtener la celda en la sexta columna (índice 5)
        var celdaPrecio = filas[i].getElementsByTagName("td")[5];

        // Obtener el valor de la celda
        var valorPrecio = parseFloat(celdaPrecio.textContent || celdaPrecio.innerText);

        // Sumar el precio al total
        sumaPrecios += valorPrecio;
    }

    console.log("Suma de precios: " + sumaPrecios);
    document.getElementById("total").innerText = sumaPrecios

}