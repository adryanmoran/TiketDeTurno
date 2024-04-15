document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        e.preventDefault(); // Evita que el formulario se envíe automáticamente
        
        // Verificar campos vacíos
        var turno = document.getElementById('turno').value;
        var id_municipio = document.getElementById('id_municipio').value;
        var id_asunto = document.getElementById('id_asunto').value;
        var fecha = document.getElementById('fecha').value;
        var proceso = document.getElementById('proceso').value;

        if (!turno || !id_municipio || !id_asunto || !fecha || !proceso) {
            // Mostrar SweetAlert si hay campos vacíos
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Por favor, completa todos los campos.',
            });
        } else {
            // Si todos los campos están completos, enviar el formulario
            this.submit();
        }
    });
});

