document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('categoryChart').getContext('2d');
    var chartLabels = Object.keys(chartData);
    var chartValues = Object.values(chartData);

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartLabels,
            datasets: [{
                label: 'Количество книг по категориям',
                data: chartValues,
                backgroundColor: 'rgba(144, 238, 144, 0.5)',
                borderColor: 'rgba(0, 128, 0, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            layout: {
                padding: {
                    top: 50
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
