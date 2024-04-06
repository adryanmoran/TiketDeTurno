// script.js
function validateForm() {
    var nombre = document.getElementById("nombre").value;
    if (nombre.trim() == "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El campo del nombre del asunto no puede estar vacío.'
        });
        return false;
    }
    return true;
}
