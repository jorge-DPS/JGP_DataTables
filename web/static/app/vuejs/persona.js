var csrf_token = { headers: { "X-CSRFToken": csrftoken } };


var app = new Vue({
    el: '#kt_personas',
    data: {
        persona:{
            primer_nombre:null,
            segundo_nombre:null,
            primer_apellido:null,
            segundo_apellido:null,
            apellido_esposo:null,
            valor_documento_identificacion:null,
            complemento:null,
            extension:null,
            
        },
        persona_edit:null,
		personas_erros:[],
	
    },
	/* computed:{
		verExtencion
	}, */ 
    methods:{
        deletePersona: function(pk){
            console.log("delete",pk)
			var url = URLS.endpoints.deletePersona(pk);
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
					self.$http.post(url, {}, _header).then(
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
        createPersona: function(){
            console.log("crear Persona", this.persona)
            var self=this;     
            Swal.fire({
                title: "¿Está seguro?",
                icon: "warning",
                showCancelButton: true,
                buttonsStyling: false,
                confirmButtonText: "Si, enviar persona!",
                cancelButtonText: "No, cancelar",
                customClass: {
                    confirmButton: "btn font-weight-bold btn-success",
                    cancelButton: "btn font-weight-bold btn-default"
                }  
            }).then(function (result) {
                if (result.value) {
                    var url = URLS.endpoints.crearListarPersona();
                    console.log(this.persona)
                    var data = self.makeFormDataPersona(self.persona);
                    self.$http.post(url, data, csrf_token).then(
                    function (response) {
                        toastr.success("La Perssona se ha almacenado correctamente", response.data);
                        //this.modal.reclamos.modal('hide');
                        window.location.href = URL_LIST;
                    },
                    function(responseError){
						this.personas_erros = responseError.body
						console.log(this.personas_erros)
                        toastr.error("ERROR: AL ENVIAR LOS DATOS", responseError.body)
                        }
                    );
                }
            });
        },
      zmakeFormDataPersona: function(data_input){
			var data = new FormData();
			if (!!data_input.primer_nombre){
				data.append("primer_nombre", data_input.primer_nombre);
			}
			if (!!data_input.segundo_nombre){
				data.append("segundo_nombre", data_input.segundo_nombre);
			} 
			if (!!data_input.primer_apellido){
				data.append("primer_apellido", data_input.primer_apellido);
			}
            if (!!data_input.segundo_apellido){
				data.append("segundo_apellido", data_input.segundo_apellido);
			}
			if (!!data_input.apellido_esposo){
				data.append("apellido_esposo", data_input.apellido_esposo);
			}
			if (!!data_input.valor_documento_identificacion){
				data.append("valor_documento_identificacion", data_input.valor_documento_identificacion);
			}
			if (!!data_input.complemento){
				data.append("complemento", data_input.complemento);
			}
			if (!!data_input.extension){
				data.append("extension", data_input.extension);
			}
			return data
		},
        getPersona:function(pk){
            var url = URLS.endpoints.editPersona(pk);
            this.$http.get(url).then(
                function (response){
                    console.log(this.persona = response.body);
                }
            )
        },
        editPersonas:function(pk){
            console.log("editarPersona", pk )
            var self = this;
			var url = URLS.endpoints.editPersona(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = self.makeFormDataPersona(self.persona);
			
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizara los datos de la Persona.",
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
					console.log("actualizando Personas", data)
					self.$http.put(url, data, _header).then(function(response) {
                    toastr.success("Se ha actualizado correctamente la persona", "<h6>Actualizacion correcto</h6>");
                    window.location.href = URL_LIST;
					}, function(responseError) {
						this.personas_erros = responseError.body
						console.log("this.personas_erros",this.personas_erros)
						toastr.error("ERROR: EL NUMERO DE DOCUMENTO YA SE ENCUENTRA REGISTRADO", responseError.body)
					});
				} 
			});
        }
    },
    mounted: function(){
        console.log(this.persona.primer_nombre)
    }
})