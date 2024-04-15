// Función para validar la contraseña
function validarContraseña() {
    var contraseña = document.getElementById('contraseña').value.trim();
    var contraseñaFeedback = document.getElementById('contraseña-feedback');
    var contraseñaInput = document.getElementById('contraseña');

    if (!/^(?=.*[a-zA-Z])(?=.*\d).{6,}$/.test(contraseña)) {
        contraseñaFeedback.innerHTML = 'La contraseña debe contener al menos una letra y un número y tener al menos 6 caracteres.';
        contraseñaInput.classList.add('error');
    } else {
        contraseñaFeedback.innerHTML = ''; // Limpia el mensaje de retroalimentación si la contraseña es válida
        contraseñaInput.classList.remove('error');
    }
}

// Función para validar que las contraseñas coincidan
function validarCoincidenciaContraseña() {
    var contraseña = document.getElementById('contraseña').value.trim();
    var confirmarContraseña = document.getElementById('confirmar_contraseña').value.trim();
    var confirmarContraseñaFeedback = document.getElementById('confirmar_contraseña-feedback');
    var confirmarContraseñaInput = document.getElementById('confirmar_contraseña');

    if (contraseña !== confirmarContraseña) {
        confirmarContraseñaFeedback.innerHTML = 'Las contraseñas no coinciden.';
        confirmarContraseñaInput.classList.add('error');
    } else {
        confirmarContraseñaFeedback.innerHTML = ''; // Limpia el mensaje de retroalimentación si las contraseñas coinciden
        confirmarContraseñaInput.classList.remove('error');
    }
}

// Llama a las funciones de validación cada vez que se modifica el campo correspondiente
document.getElementById('contraseña').addEventListener('input', validarContraseña);
document.getElementById('confirmar_contraseña').addEventListener('input', validarCoincidenciaContraseña);

// Función para validar el formulario
function validarFormulario() {
    var usuario = document.getElementById('usuario').value.trim();
    var contraseña = document.getElementById('contraseña').value.trim();
    var confirmarContraseña = document.getElementById('confirmar_contraseña').value.trim();
    var nombreCompleto = document.getElementById('nombre_completo').value.trim();
    var puesto = document.getElementById('puesto').value.trim();

    if (usuario === '') {
        Swal.fire('Error', 'Por favor completa el campo Usuario.', 'error');
        return false;
    } else if (contraseña === '') {
        Swal.fire('Error', 'Por favor completa el campo Contraseña.', 'error');
        return false;
    } else if (!/^(?=.*[a-zA-Z])(?=.*\d).{6,}$/.test(contraseña)) {
        Swal.fire('Error', 'La contraseña debe contener al menos una letra y un número y tener al menos 6 caracteres.', 'error');
        return false;
    } else if (contraseña !== confirmarContraseña) {
        Swal.fire('Error', 'Las contraseñas no coinciden.', 'error');
        return false;
    } else if (nombreCompleto === '') {
        Swal.fire('Error', 'Por favor completa el campo Nombre Completo.', 'error');
        return false;
    } else if (puesto === '') {
        Swal.fire('Error', 'Por favor completa el campo Puesto.', 'error');
        return false;
    } else {
        return true;
    }
}
