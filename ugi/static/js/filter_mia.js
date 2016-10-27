// When the document is ready
  $(document).ready(function () {

      $('#filter1').datepicker({
          format: "yyyy-mm-dd"
      });
      $('#filter2').datepicker({
          format: "yyyy-mm-dd"
      });


      $( "#filter_date" ).click(function() {
        // console.log($('#filter1').val());

      $.ajax({
         url : "/filter_date/", // the endpoint
         type : "GET", // http method
         data : { the_post : $('#filter1').val(), the_post2:  $('#filter2').val() }, // data sent with the post request

         // handle a successful response
         success : function(json) {
             $('#post-text').val(''); // remove the value from the input
             // console.log(json); // log the returned json to the console
             // console.log("success"); // another sanity check

        /* ############ REQUIREMENTS #################
          models ==> tipo_instalacion (Y)

        */


             $('#container').highcharts({
                 chart: {
                     type: 'column'
                 },
                 title: {
                     text: 'Reporte'
                 },
                 xAxis: {
                     categories: ['Línea Base', 'Ingresados', 'Resueltos', 'Exp. Trámite']
                 },
                 yAxis: {
                     min: 0,
                     title: {
                         text: 'TOTAL EN TRÁMITE'
                     },
                     stackLabels: {
                         enabled: true,
                         style: {
                             fontWeight: 'bold',
                             color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                         }
                     }
                 },
                 legend: {
                     align: 'right',
                     x: -30,
                     verticalAlign: 'top',
                     y: 25,
                     floating: true,
                     backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
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
                             enabled: true,
                             color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
                         }
                     }
                 },
                 series: [{
                     name: 'Trasnporte',
                     data: [5, 3, 4, 7]
                 }, {
                     name: 'Red de distribución',
                     data: [2, 2, 3, 2]
                 }, {
                     name: 'Estación de carburación',
                     data: [3, 4, 4, 2]
                 }, {
                     name: 'COFEMER',
                     data: [3, 4, 4, 2]
                 },  {
                     name: 'Compresión',
                     data: [3, 4, 4, 2]
                 }]
             });
         },

         // handle a non-successful response
         error : function(xhr,errmsg,err) {
             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
         }
     });
   });



  });
