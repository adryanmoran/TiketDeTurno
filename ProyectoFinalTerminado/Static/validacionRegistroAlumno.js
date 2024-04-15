
function validarFormulario() {
    var nombreCompleto = document.getElementById("nombre_completo").value;
    var curp = document.getElementById("curp").value;
    var nombre = document.getElementById("nombre").value;
    var apellidoPaterno = document.getElementById("paterno").value;
    var apellidoMaterno = document.getElementById("materno").value;
    var telefono = document.getElementById("telefono").value;
    var celular = document.getElementById("celular").value;
    var correo = document.getElementById("correo").value;
    var nivel = document.getElementById("nivel_id").value;
    var municipio = document.getElementById("municipio_id").value;
    var asunto = document.getElementById("asunto_id").value;

    // Expresiones regulares para validar formato
    var curpRegex = /^[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}$/;
    var telefonoRegex = /^[0-9]{10}$/;
    var celularRegex = /^[0-9]{10}$/;
    var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validaciones
    if (nombreCompleto === "") {
        Swal.fire("Error", "Por favor, ingresa tu nombre completo.", "error");
    } else if (curp === "") {
        Swal.fire("Error", "Por favor, ingresa tu CURP.", "error");
    } else if (!curpRegex.test(curp)) {
        Swal.fire({
            title: "Error",
            text: "El CURP ingresado no es válido. Por favor, verifica e inténtalo de nuevo.",
            icon: "error",
            showCancelButton: true,
            confirmButtonText: "Buscar CURP",
            cancelButtonText: "Cancelar",
            cancelButtonColor: "#d33",
        }).then((result) => {
            if (result.isConfirmed) {
                window.open("https://www.bing.com/search?pglt=43&q=curp&cvid=462ea063f5d147bbb316b9325c3ecded&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgxMjIwajBqMagCCLACAQ&FORM=ANNTA1&ucpdpc=UCPD&PC=U531");
            }
        });
    } else if (nombre === "") {
        Swal.fire("Error", "Por favor, ingresa tu nombre.", "error");
    } else if (apellidoPaterno === "") {
        Swal.fire("Error", "Por favor, ingresa tu apellido paterno.", "error");
    } else if (apellidoMaterno === "") {
        Swal.fire("Error", "Por favor, ingresa tu apellido materno.", "error");
    } else if (telefono === "") {
        Swal.fire("Error", "Por favor, ingresa tu teléfono.", "error");
    } else if (!telefonoRegex.test(telefono)) {
        Swal.fire("Error", "Por favor, ingresa un número de teléfono válido (10 dígitos sin espacios ni caracteres especiales).", "error");
    } else if (celular === "") {
        Swal.fire("Error", "Por favor, ingresa tu número de celular.", "error");
    } else if (!celularRegex.test(celular)) {
        Swal.fire("Error", "Por favor, ingresa un número de celular válido (10 dígitos sin espacios ni caracteres especiales).", "error");
    } else if (correo === "") {
        Swal.fire("Error", "Por favor, ingresa tu correo electrónico.", "error");
    } else if (!correoRegex.test(correo)) {
        Swal.fire("Error", "Por favor, ingresa una dirección de correo electrónico válida.", "error");
    } else if (nivel === "") {
        Swal.fire("Error", "Por favor, selecciona un nivel.", "error");
    } else if (municipio === "") {
        Swal.fire("Error", "Por favor, selecciona un municipio.", "error");
    } else if (asunto === "") {
        Swal.fire("Error", "Por favor, selecciona un asunto.", "error");
    } else {
        // Si pasa todas las validaciones, enviar el formulario
        Swal.fire("¡Éxito!", "¡El formulario se ha enviado correctamente!", "success");
        document.getElementById("formularioContacto").submit();
    }
}
