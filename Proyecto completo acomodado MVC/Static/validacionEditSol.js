// ValEditNivel.js
function validarFormulario() {
    var nombre = document.getElementById('nombre').value.trim();

    if (nombre === '') {
        Swal.fire({
            icon: 'error',
            title: 'Campo vacío',
            text: 'Por favor, introduce un nombre para el nivel.'
        });
        return false;
    }

    return true;
}
