$(document).ready(function() {
    // Llamada AJAX para obtener datos de las gráficas
    $.ajax({
        type: 'GET',
        url: '/data',
        success: function(data) {
            // Procesar los datos y dibujar la gráfica utilizando Plotly.js
            // Por simplicidad, vamos a dibujar una gráfica de barras
            var municipios = Object.keys(data);
            var estados = ['Resuelto', 'Pendiente'];
            var datos = [];

            estados.forEach(function(estado) {
                var valores = municipios.map(function(municipio) {
                    return data[municipio][estado];
                });

                datos.push({
                    x: municipios,
                    y: valores,
                    type: 'bar',
                    name: estado
                });
            });

            var layout = {
                title: 'Estatus de las Solicitudes por Municipio',
                barmode: 'stack'
            };

            Plotly.newPlot('grafica', datos, layout);
        }
    });
});
