// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Selecciona el formulario
    var form = document.getElementById('editForm');

    // Agrega un listener para el evento submit del formulario
    form.addEventListener('submit', function(event) {
        // Evita el comportamiento predeterminado de enviar el formulario
        event.preventDefault();

        // Obtiene el valor del campo de entrada
        var nombre = document.getElementById('nombre').value;

        // Valida si el campo está vacío o solo contiene espacios en blanco
        if (nombre.trim() === '') {
            // Muestra SweetAlert si el campo está vacío
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, introduce un nombre para el nivel.',
            });
        } else {
            // Envía el formulario si el campo no está vacío
            form.submit();
        }
    });
});
