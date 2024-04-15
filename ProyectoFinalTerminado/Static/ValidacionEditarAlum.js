function validarFormulario() {
    var nombreCompleto = document.getElementById('nombre_completo').value;
    var nombre = document.getElementById('nombre').value;
    var paterno = document.getElementById('paterno').value;
    var materno = document.getElementById('materno').value;
    var telefono = document.getElementById('telefono').value;
    var celular = document.getElementById('celular').value;
    var correo = document.getElementById('correo').value;

    var telefonoPattern = /^\d{10}$/; // Se espera un número de 10 dígitos
    var celularPattern = /^\d{10}$/; // Se espera un número de 10 dígitos
    var correoPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Expresión regular para validar un formato de correo electrónico básico

    if (nombreCompleto === '') {
        Swal.fire('Error', 'Por favor completa el campo Nombre Completo.', 'error');
        return false;
    } else if (nombre === '') {
        Swal.fire('Error', 'Por favor completa el campo Nombre.', 'error');
        return false;
    } else if (paterno === '') {
        Swal.fire('Error', 'Por favor completa el campo Apellido Paterno.', 'error');
        return false;
    } else if (materno === '') {
        Swal.fire('Error', 'Por favor completa el campo Apellido Materno.', 'error');
        return false;
    } else if (telefono === '') {
        Swal.fire('Error', 'Por favor completa el campo Teléfono.', 'error');
        return false;
    } else if (!telefono.match(telefonoPattern)) {
        Swal.fire('Error', 'Por favor ingresa un número de teléfono válido.', 'error');
        return false;
    } else if (celular === '') {
        Swal.fire('Error', 'Por favor completa el campo Celular.', 'error');
        return false;
    } else if (!celular.match(celularPattern)) {
        Swal.fire('Error', 'Por favor ingresa un número de celular válido.', 'error');
        return false;
    } else if (correo === '') {
        Swal.fire('Error', 'Por favor completa el campo Correo Electrónico.', 'error');
        return false;
    } else if (!correo.match(correoPattern)) {
        Swal.fire('Error', 'Por favor ingresa un correo electrónico válido.', 'error');
        return false;
    } else {
        return true;
    }
}