Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Productos por categorias vendidos'
    },
    xAxis: {
        categories: ['Hamburguesas/Tortas', 'Comida Mexicana', 'Bebidas']
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Unidades Vendidas'
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                ) || 'gray'
            }
        }
    },
    legend: {
        align: 'right',
        x: -30,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true
            }
        }
    },
    series: [{
        name: 'Torta de Carne',
        data: [19, 0, 0]
    }, {
        name: 'Torta de Jamon',
        data: [43, 0, 0]
    },
     {
        name: 'Coca Cola',
        data: [0, 0, 34]
    },
    {
        name: 'Pepsi',
        data: [0, 0, 34]
    },{
        name: 'Tacos',
        data: [0, 44, 0]
    }]
});