var csrf_token = { headers: { "X-CSRFToken": csrftoken } };

var CONTRATO = {
  codigo_operacion: null,
  sucursal_id: null,
  fecha_desembolso: null,
  deudores: null,
  garantias_reales: null,
  monto_desembolso: null,
  tasa_interes_mensual: null,
  numero_cuotas: null,
  frecuencia: null,
  monto_cargos: null,
  tipo_garantia: null,
  destino_prestamo: null,
  nombre_grupo: null,
  testimonio_poder_id: null,
  planilla_contrato: "version2/contrato/etc",
  datos_operacion: null,
};
var app = new Vue({
  el: '#kt_content_contrato',
  data: {
    contrato:null,
    deudores:{
      'nombre': null,
      'ci': null,
      'genero': null,
      'estado_civil': null,
      'direccion': null,
      'tipo_obligacion': null,
    },
    contrato_completo: CONTRATO,
    contrato_find: null,
    testimonio_poder: null,
    loader: false,
    codigo_operacion: "501211100594",
    data_cliente:null,
    contrato_edit:null,
  },
  computed: {
    numeralaliteral: function(){
			return NumerosaLetras(NUMERALITERAL);
		},
    porcentaje: function(){
			return Porcentaje(PORCENTAJE);
		},
    nrocuotas: function(){
			return NumLetras(NROCUOTAS);
		},
    cargos: function(){
			return NumerosaLetras(CARGOS);
		},
  },
  methods: {
    printContrato: function () {
      console.log("Imprimir");
      print();
    },
    loadContrato: function () {
      if (!!this.codigo_operacion) {
        var url = URLS.endpoints.getContrato(this.codigo_operacion);
        this.loader=true; 
        this.contrato = null;
        this.$http.get(url).then(
          function (response) {
            this.contrato = response.body.data;
            toastr.success("Codigo de operacion encontrado y cargado");
            this.loader=false;
          },
          function (responseError) {
            console.log("ERROR", responseError);
            toastr.error("El codigo de operacion no se ha encontrado");
            this.loader=false;
          }
        ).catch(function (response) {
          console.log("CATCH", response);
        })
        .finally(function () {
          this.loader=false;
          this.loader = false;
        });
			}else {
					toastr.error("Ingrese el Codigo de operacion primero", "Error!");
			}
		},
    setContrato: function(data){
      console.log(data);
      var self = this;

      if(!!data.codigo_operacion){
        this.contrato_completo.codigo_operacion = data.codigo_operacion;
      }
      if(!!data.codigo_oficina){
        this.contrato_completo.sucursal_id = data.codigo_oficina;
      }
      if(!!data.fecha_desembolso){
        this.contrato_completo.fecha_desembolso = data.fecha_desembolso;
      }
      if(!!data.deudores){
        this.contrato_completo.deudores = data.deudores;
      }
      if(!!data.garantias){
        this.contrato_completo.garantias_reales = data.garantias;
      }
      if(!!data.monto_desembolsado){
        this.contrato_completo.monto_desembolso = data.monto_desembolsado;
      }
      if(!!data.tasa_interes_mensual){
        this.contrato_completo.tasa_interes_mensual = data.tasa_interes_mensual;
      }
      if(!!data.numero_cuotas){
        this.contrato_completo.numero_cuotas = data.numero_cuotas;
      }
      if(!!data.frecuencia){
        this.contrato_completo.frecuencia = data.frecuencia;
      }
      if(!!data.monto_cargos){
        this.contrato_completo.monto_cargos = data.monto_cargos;
      }
      if(!!data.tipo_garantia){
        this.contrato_completo.tipo_garantia = data.tipo_garantia;
      }
      if(!!data.motivo_prestamo){
        this.contrato_completo.destino_prestamo = data.motivo_prestamo;
      }
      if(!!data.descripcion_grupo){
        this.contrato_completo.nombre_grupo = data.descripcion_grupo;
      }
      if(!!data.codigo_oficina){
        self.loadEncargado(this.contrato_completo.sucursal_id);
        console.log("----------------->", this.contrato_completo.testimonio_poder_id );
      }
      if(!!data.planilla_contrato){
        this.contrato_completo.planilla_contrato = planilla_contrato;
      }
      console.log("encargado poder===>",this.contrato_completo.testimonio_poder_id )  
      return this.contrato_completo;
    },
    saveContrato: function () {
      console.log("saveContrato");
      this.setContrato(this.contrato);
            
      var self=this;
      Swal.fire({
        title: "¿Está seguro?",
        icon: "warning",
        showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "Si, guardar!",
        cancelButtonText: "No, cancelar",
        customClass: {
            confirmButton: "btn font-weight-bold btn-success",
            cancelButton: "btn font-weight-bold btn-default"
        }
      }).then(function (result) {
        if (result.value) {
          var url = URLS.endpoints.postContrato();
          console.log(this.contrato_completo);
          var data = self.contrato_completo;

          console.log("====>",data, url)
          self.$http.post(url, data, csrf_token).then(function (response) {
              toastr.success("El contrato se ha almacenado correctamente");
              window.location.href = URL_LIST;
            },
            function (responseError) {
              //self.contrato_errors = responseError.body;
              toastr.error("El contrato NO se ha almacenado correctamente");
              console.log(responseError.body)
          });
        }
      });
    },
    loadEncargado: function(codigo_oficina){
      console.log("****** Cargando lista de encargados ******", codigo_oficina)
			var url = URLS.endpoints.getEncargadoPoder(codigo_oficina);

			this.$http.get(url).then(
				function(response) {
          this.contrato_completo.testimonio_poder_id = response.body.id;
          console.log("******", this.contrato_completo.testimonio_poder_id );
				},        
				function(responseError) {
					console.log("ERROR");
					console.log(responseError);
				}
			);
		},
    deleteContrato: function (pk) {
			var url = URLS.endpoints.deleteContrato(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se eliminara el contrato y todos sus datos.",
				icon: "warning",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, eliminar!",
				cancelButtonText: "No, cancelar",
				customClass: {
					confirmButton: "btn font-weight-bold btn-danger",
					cancelButton: "btn font-weight-bold btn-default"
				}
			}).then(function (result) {
				if (result.value) {
					self.$http.put(url, {}, _header).then(
						function (response) {
							console.log("eliminado")
						},
						function (responseError) {
							console.log("ERROR eliminado")
						}
					);
					window.location.href = URL_LIST;
				}
			});
		},
    getContrato:function(pk){
      self=this;      
      console.log("cargando datos en edit");
      var url = URLS.endpoints.editContrato(pk);
      this.$http.get(url).then(
          function (response){
              self.contrato = response.body;
              console.log(self.contrato);
              self.codigo_operacion = self.contrato.codigo_operacion
              self.loadContrato();
              self.contrato_completo.datos_operacion=self.contrato;
          }
      )
    },
    editContratos:function(pk){
      console.log("editarContrato", pk )
      var self = this;
      var url = URLS.endpoints.editContrato(pk);
      var _header = { headers: { "X-CSRFToken": csrftoken } };
      var data = self.setContrato(self.contrato);

      Swal.fire({
        title: "¿Está seguro?",
        text: "Se actualizara los datos del Contrato.",
        icon: "warning",
        showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "Si, actualizar",
        cancelButtonText: "No, cancelar",
        customClass: {
          confirmButton: "btn font-weight-bold btn-success",
          cancelButton: "btn font-weight-bold btn-default"
        }
      }).then(function(result) {
        if (result.value) {
          console.log("actualizando Contrato", data)
          self.$http.put(url, data, _header).then(function(response) {
                    toastr.success("Se ha actualizado correctamente el contrato", "<h6>Actualizacion correcto</h6>");
                    window.location.href = URL_LIST;
          }, function(responseError) {
            console.log(responseError)
          });
        } 
      });
    },
  },
  mounted: function ()
  {
    //this.loadEncargado();
    //console.log("Cargando vueJS");
    //console.log(this.data_cliente.estado_civil);
  },

})
