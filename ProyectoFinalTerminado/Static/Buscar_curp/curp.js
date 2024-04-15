function validateForm() {
    var curp = document.getElementById("curp_buscar").value;
    var curpRegex = /^[A-Z]{4}[0-9]{6}[HM]{1}[A-Z]{5}[A-Z0-9]{2}$/;
    if (curp == "") {
        Swal.fire({
            icon: 'error',
            title: 'Campo vacío',
            text: 'Por favor ingrese una CURP para buscar.'
        });
        return false;
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
        return false;
    }
    return true;
}
