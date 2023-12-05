document.addEventListener("DOMContentLoaded", function() {
    var csrftoken = getCookie('csrftoken');

    // Listener al botón de guardar
    var btnGuardar = document.getElementById("btnGuardar");
    btnGuardar.addEventListener("click", function() {
        var usuario = document.getElementById("titulo").getAttribute('nombre-usuario');
        var nombre = document.getElementById("txtNombre").value;
        var apellido = document.getElementById("txtApellido").value;
        var email = document.getElementById("txtEmail").value;
        var contrasena = document.getElementById("txtContrasena").value;

      
        $.ajax({
            url: '/actualizarDatos/' + usuario + '/' + nombre + '/' + apellido + '/' + email +'/' + contrasena + '/',
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                console.log('datos actualizados');  
                alert('Datos Actualizados')
            },
            error: function(error) {
                console.error('Error al obtener guardar nuevos datos', error);
            }
        });
    });

    // Listener al botón de eliminar
    var btnEliminar = document.getElementById("btnEliminar");
    btnEliminar.addEventListener("click", function() {
        var usuario = document.getElementById("titulo").getAttribute('nombre-usuario');

        $.ajax({
            url: '/eliminarCuenta/' + usuario + '/',
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                console.log('usuario borrado');  
                window.location.href = '/irLogin/';

            },
            error: function(error) {
                console.error('Error al eliminar usuario', error);
            }
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
