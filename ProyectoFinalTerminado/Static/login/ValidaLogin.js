
        function validateForm() {
            var usuario = document.getElementById("usuario").value;
            var contraseña = document.getElementById("contraseña").value;
            var recaptcha = document.getElementById("g-recaptcha-response").value;

            if (usuario.trim() === "") {
                Swal.fire({
                    icon: 'error',
                    title: 'Campo vacío',
                    text: 'Por favor ingresa tu usuario.'
                });
                return false;
            }

            if (contraseña.trim() === "") {
                Swal.fire({
                    icon: 'error',
                    title: 'Campo vacío',
                    text: 'Por favor ingresa tu contraseña.'
                });
                return false;
            }

            if (recaptcha === "") {
                Swal.fire({
                    icon: 'error',
                    title: 'Recaptcha no completado',
                    text: 'Por favor completa el recaptcha.'
                });
                return false;
            }

            return true;
        }
