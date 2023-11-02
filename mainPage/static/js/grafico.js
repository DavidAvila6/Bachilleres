// Obtener el contexto del canvas
var ctx = document.getElementById('desertionChart').getContext('2d');

// Datos del gráfico (ejemplo)
var data = {
    labels: ['Año 2020', 'Año 2021', 'Año 2022', 'Año 2023'],
    datasets: [{
        label: 'Tasa de Deserción Escolar',
        data: [10, 8, 6, 5],
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

// Configuración del gráfico
var chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

// Crear el gráfico de barras
var desertionChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: chartOptions
});
