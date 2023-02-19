var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
var ID_DEPOSITO = DEPOSITO;
var SELECT = SELECT2;
/* var DEPOSITOS = {
	'codigo_operacion': null,
	'fecha_deposito': null,
	'monto_depositado': null,
	'concepto': null,
	'observaciones': null,
	'banco': null,
	'comprobante': "Remove photo",
	'estado': null,
	'sucursal_creacion': null,
	'codigo_asesor': null,
}; */
var app = new Vue({
	el: '#kt_depositos',
	data: {
		deposito: {
			codigo_operacion: null,
			fecha_deposito: null,
			monto_depositado: null,
			concepto: null,
			observaciones: null,
			banco: null,
			comprobante:false,
			estado: null,
			sucursal_creacion: null,
			codigo_asesor: null,
			aplicado: false,
		},
    error_deposito: {
			banco: null,
      codigo_operacion: null,
			comprobante:false,
			concepto: null,
			fecha_deposito: null,
			monto_depositado: null,
    },
		//deposito_edit: DEPOSITOS,
		prueba: null,
		deposito_edit: null,
		deposito_estado:null,
		nombreAsesor:null,
		code_rol:null
	},
	created(){
		console.log("Life-Cicle: created")
	},
  computed: {
    errorCodigoOperacion() {
      if (!!this.error_deposito.codigo_operacion){
        return {
          'has-error': true,
          'border': true,
          'border-danger': true,
        };
      }
      return false;
    },

		buildImageUrl: function () {
			return 'background-image: url(" ' + this.deposito.comprobante + '") '
		},
    fechaDeposito: function () {
      if (this.deposito.fecha_deposito) {
        return this.deposito.fecha_deposito.split(' ')[0];
      }
      return null;
    }
	},
	methods: {
		deleteDeposito: function (pk) {
			console.log("asdasdas",pk)
			var url = URLS.endpoints.deleteDeposito(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se eliminara el deposito y todos sus datos.",
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
							console.log("eliminado", response)
						},
						function (responseError) {

							console.log("ERROR eliminado")
						}
					);
					window.location.href = URL_LIST;
				}
			});
		},
		editDeposito: function(pk) {
			/**
			 * edit depopsito
			 */
			if (!!this.$refs.avatarFile && this.$refs.avatarFile.files.length > 0) {
				this.deposito.comprobante = this.$refs.avatarFile.files[0];
				
			}
			var self = this;
			console.log("Depositos",pk);
			
			var url = URLS.endpoints.getEditDeposito(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = self.makeFormDataDeposito(self.deposito);
			
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizara los datos del deposito.",
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
					console.log("actualizando depositos", data)
					self.$http.put(url, data, _header).then(function(response) {
					  toastr.success("Se ha actualizado correctamente el activo fijo", "<h6>Actualizacion correcto</h6>");
					  window.location.href = URL_LIST;
					}, function(responseError) {
						console.log(responseError)
					});
				} 
			});   
		},
		verificarDeposito: function(pk) {
			/**
			 * edit depopsito
			 */
			var self = this;
			console.log("Depositos",pk);
			
			var url = URLS.endpoints.getVerificarDeposito(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = self.deposito;

			console.log("pk", pk)
			
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizarna los datos del deposito.",
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
					console.log("actualizando depositos", data)
					self.$http.put(url, data, _header).then(function(response) {
					  toastr.success("Se ha actualizado correctamente el activo fijo", "<h6>Actualizacion correcto</h6>");
					  window.location.href = URL_LIST;
					}, function(responseError) {
						console.log(responseError)
					});
				} 
			});   
		},
		AplicarDeposito: function(pk) {
			/**
			 * edit depopsito
			 */
			var self = this;
			console.log("Depositos",pk);
			
			var url = URLS.endpoints.getAplicadoDeposito(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = self.deposito;

			console.log("pk", pk)
			
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizarna los datos del deposito.",
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
					self.$http.put(url, data, _header).then(function(response) {
					  toastr.success("Se ha actualizado correctamente el activo fijo", "<h6>Actualizacion correcto</h6>");
					  window.location.href = URL_LIST;
					}, function(responseError) {
						console.log(responseError)
					});
				} 
			});   
		},
		getDeposito: function(pk){
			var url = URLS.endpoints.getEditDeposito(pk);
			this.$http.get(url).then(
				function (response){
          this.deposito = response.body;
				}
			)
		},
		getVerificacion: function(){
			Swal.fire({
				title: "¿Está seguro?",
				icon: "info",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, enviar deposito!",
				cancelButtonText: "No, cancelar",
				customClass: {
					confirmButton: "btn font-weight-bold btn-success",
					cancelButton: "btn font-weight-bold btn-default"
				}
				
			})	
		},
		sendDeposito: function(){
		var self=this;        
      Swal.fire({
        title: "¿Está seguro?",
        icon: "warning",
        showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "Si, enviar deposito!",
        cancelButtonText: "No, cancelar",
        customClass: {
            confirmButton: "btn font-weight-bold btn-success",
            cancelButton: "btn font-weight-bold btn-default"
        }
          
      }).then(function (result) {
        if (result.value) {
          var url = URLS.endpoints.crearListarDeposito();
          var data = self.makeFormDataDeposito(self.deposito);
          self.$http.post(url, data, csrf_token).then(
            function (response) {
              toastr.success("El deposito se ha almacenado correctamente", response.data);
              //this.modal.reclamos.modal('hide');
              window.location.href = URL_LIST;
          },
          function(responseError){
              console.log(responseError);
              self.error_deposito = responseError.body;
              //toastr.error("ERROR", responseError.body)
            }
          );
        }
      });
		},
		listDepositos: function(){
			let url = URLS.endpoints.crearListarDeposito();
			this.$http.get(url).then(
				function (response) {
					//console.log(response.body)
				}
			)	
		},
		makeFormDataDeposito: function(data_input){
			var data = new FormData();
			if (!!data_input.codigo_operacion){
				data.append("codigo_operacion", data_input.codigo_operacion);
			}
	
			if (!!data_input.fecha_deposito){
				data.append("fecha_deposito", data_input.fecha_deposito);
			} 
	
			if (!!data_input.monto_depositado){
				data.append("monto_depositado", data_input.monto_depositado);
			}
	
			if (!!data_input.concepto){
				data.append("concepto", data_input.concepto);
			}
	
			if (!!data_input.observaciones){
				data.append("observaciones", data_input.observaciones);
			}		
	
			if (!!data_input.banco){
				data.append("banco", data_input.banco);
			}
	
			if (!!this.$refs.avatarFile.files.length > 0){
				//console.log("comprobante:",  this.$refs.avatarFile.files);
				data.append("comprobante", this.$refs.avatarFile.files[0]);
			}else{
				console.log("notiene imagen");
			}
			if (!!data_input.estado){
				data.append("estado", data_input.estado);
			}
			if (!!data_input.sucursal_creacion){
				data.append("sucursal_creacion", data_input.sucursal_creacion);
			}
			if (!!data_input.codigo_asesor){
				data.append("codigo_asesor", data_input.codigo_asesor);
			}
			if (!!data_input.aplicado){
				data.append("aplicado", data_input.aplicado);
			}
			
			return data
	
		},

	},
	
	mounted: function () {
    //this.getDeposito(DEPOSITO);
		//console.log("DEPOSITO: ",this.deposito);
    
	},
});
