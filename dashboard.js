const ctx = document.getElementById('consumptionChart');

new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
      label: 'Food Consumption (kg)',
      data: [80, 85, 78, 90, 88, 92, 85],
      borderWidth: 2
    }]
  }
});
