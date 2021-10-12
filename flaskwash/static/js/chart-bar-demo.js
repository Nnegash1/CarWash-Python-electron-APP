var ctx = document.getElementById('myBarChart').getContext('2d');
var mychar = new Chart(ctx, {
    type: 'bar',
    data:{
        label: ['Red', 'Blue', 'Yellow'],
        datasets: [{
            label: '# of Votes',
            data:[12,10,13],
            backgroundColor:[
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
            ],
            borderColor:[
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
            ],
            borderWidth:1
        }]
    },
    option: {
        scales:{
            y:{
                beginAtZero: true
            }
        }
    }
});
