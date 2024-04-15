document.addEventListener('DOMContentLoaded', function() {
    var nivelesList = document.getElementById('niveles-list');
    var button = document.getElementById('load-niveles');
    var isListVisible = false;

    // Función para crear un nuevo nivel
    document.getElementById('create-form').onsubmit = function(event) {
        event.preventDefault();
        var nombreNivel = document.getElementsByName('NombreNivel')[0].value;
        
        fetch('/niveles', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({NombreNivel: nombreNivel})
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            // Actualizar la lista de niveles
            loadNiveles();
        })
        .catch(error => console.error('Error:', error));
    };

    // Función para actualizar un nivel existente
    document.getElementById('update-form').onsubmit = function(event) {
        event.preventDefault();
        var idNivel = document.getElementsByName('idNivel')[0].value;
        var nombreNivel = document.getElementsByName('NombreNivel')[1].value;
        
        fetch('/niveles/' + idNivel, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({NombreNivel: nombreNivel})
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            // Actualizar la lista de niveles
            loadNiveles();
        })
        .catch(error => console.error('Error:', error));
    };

    // Función para eliminar un nivel
    document.getElementById('delete-form').onsubmit = function(event) {
        event.preventDefault();
        var idNivel = document.getElementsByName('idNivel')[1].value;
        
        fetch('/niveles/' + idNivel, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            // Actualizar la lista de niveles
            loadNiveles();
        })
        .catch(error => console.error('Error:', error));
    };

    // Función para cargar y mostrar todos los niveles
    button.onclick = function() {
        if (isListVisible) {
            nivelesList.style.display = 'none';
            isListVisible = false;
        } else {
            loadNiveles();
            isListVisible = true;
        }
    };

    // Función para cargar los niveles
    function loadNiveles() {
        fetch('/niveles')
        .then(response => response.json())
        .then(data => {
            nivelesList.innerHTML = '';
            data.niveles.forEach(function(nivel) {
                var li = document.createElement('li');
                li.textContent = nivel.NombreNivel; // Asegúrate de que esto coincida con cómo se devuelven los datos de tu API
                nivelesList.appendChild(li);
            });
            nivelesList.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    }

    // Asegúrate de llamar a la función loadNiveles cuando se cargue la página y después de cada operación CRUD
    loadNiveles(); // Esto cargará el listado de niveles cuando se cargue la página
});