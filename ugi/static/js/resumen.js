<script>
    var jsonObject = JSON.parse('{{ time_series_json_string | escapejs }}');
    console.log(jsonObject);
    
    Highcharts.chart('resumen', {
           chart: {
               type: 'column',
               options3d: {
                   enabled: true,
                   alpha: 15,
                   beta: 15,
                   viewDistance: 25,
                   depth: 40
               }
           },

           title: {
               text: 'Reporte bimestral'
           },

           xAxis: {
               categories: ['1er Bimestre', '2do Bimestre', '3er Bimestre', '4to Bimestre', '5to Bimestre']
           },

           yAxis: {
               allowDecimals: false,
               min: 0,
               title: {
                   text: 'Número de total trámites'
               }
           },

           tooltip: {
               headerFormat: '<b>{point.key}</b><br>',
               pointFormat: '<span style="color:{series.color}">\u25CF</span> {series.name}: {point.y} / {point.stackTotal}'
           },

           plotOptions: {
               column: {
                   stacking: 'normal',
                   depth: 40
               }
           },

           series: [{
               name: 'Resueltos',
               data: [5, 3, 4, 7, 2],
               stack: 'male'
           }, {
               name: 'En trámite',
               data: [3, 4, 4, 2, 5],
               stack: 'male'
           }]
       });
</script>
