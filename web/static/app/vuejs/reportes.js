//var csrf_token = { headers: { "X-CSRFToken": csrftoken } };

var app = new Vue({
	el: '#id_reporte',
	data: {
    listaReporte: null,
	},
 
  methods: {
    listaReporteData:function (){
      console.log("*********reportes**********")
      
      //var url = URLS.endpoints.getSucursales();
      var url = URLS.endpoints.getReporteData();

      this.$http.get(url).then(
        function(response)
        {
          this.listaReporte = response.body; 
          console.log("******---", this.listaReporte);
        },        
        function(responseError) 
        {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
  },
  mounted: function(){
    console.log("MOUNTED", this.listaReporte)
    this.listaReporteData();
    //this.getDataPagina(1)
    //this.getNextPage();
  },
});
