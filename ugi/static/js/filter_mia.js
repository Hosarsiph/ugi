// When the document is ready
  $(document).ready(function () {

      $('#filter1').datepicker({
          format: "yyyy-mm-dd"
      });
      $('#filter2').datepicker({
          format: "yyyy-mm-dd"
      });
      $('#month').datepicker({
          format: "mm"
      });



      $( "#filter_date" ).click(function() {
        // console.log($('#filter1').val());

      $.ajax({
         url : "/filter_date/", // the endpoint
         type : "GET", // http method
         data : { the_post : $('#filter1').val(), the_post2:  $('#filter2').val(), month:  $('#month').val() }, // data sent with the post request

         // handle a successful response
         success : function(json) {
             $('#post-text').val(''); // remove the value from the input
             console.log(json); // log the returned json to the console
             // console.log("success"); // another sanity check


          /*   */
          Highcharts.chart('container', {
            chart: {
                type: 'pie',
                options3d: {
                    enabled: true,
                    alpha: 45,
                    beta: 0
                }
            },
            title: {
                text: 'Ingreso de trámites de ' + $('#filter1').val() + ' a ' +  $('#filter2').val()
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    depth: 35,
                    dataLabels: {
                        enabled: true,
                        format: '{point.name}'
                    }
                }
            },
            series: [{
                type: 'pie',
                name: 'Browser share',
                data: json
            }]
        });

          /*   */

          myRecords = [
                  {
                    "band": "Weezer",
                    "song": "El Scorcho"
                  },
                  {
                    "band": "Chevelle",
                    "song": "Family System"
                  }
                ]
          $('#table_query').dynatable({
            dataset: {
              records: myRecords
            }
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
