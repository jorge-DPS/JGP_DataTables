var csrf_token = { headers: { "X-CSRFToken": csrftoken } };


var app = new Vue({
    el: '#kt_consulta',
    data: {
        consulta:{
            persona:null,
            codigo_usuario:null,
            resultado:null,
            observaciones:null,
            infocred:null,    
        },
		consulta_errors:[],
		consulta_edit:null

    },
    methods:{
		getConsulta: function(pk){
			let url = URLS.endpoints.DetalleConsulta(pk);
			this.$http.get(url).then(
                function (response){
                    console.log("this.consulta = response.body",this.consulta = response.body);
                }
            )
		},

        createConsulta: function(){
            console.log("hola")
            
            var self=this;     
            Swal.fire({
                title: "¿Está seguro?",
                icon: "warning",
                showCancelButton: true,
                buttonsStyling: false,
                confirmButtonText: "Si, enviar consulta!",
                cancelButtonText: "No, cancelar",
                customClass: {
                    confirmButton: "btn font-weight-bold btn-success",
                    cancelButton: "btn font-weight-bold btn-default"
                }  
            }).then(function (result) {
				if (result.value) {
					var url = URLS.endpoints.crearListarConsulta();
					console.log(this.consulta	)
					var data = self.makeFormDataConsulta(self.consulta);
					self.$http.post(url, data, csrf_token).then(
					function (response) {
						toastr.success("La consulta se ha almacenado correctamente", response.data);
						//this.modal.reclamos.modal('hide');
						window.location.href = URL_LIST;
				},
				function(responseError){
					this.consulta_errors =responseError.body 
					console.log("responseError.body",this.consulta_errors)
					toastr.error("ERROR", responseError.body)
					}
				);
			}
			});
        },
        ListarPersona:function(){
            let url = URLS.endpoints.ListaPersona();
			this.$http.get(url).then(
				function (response) {
					this.consulta_list=response.body.results
                    console.log(JSON.parse(JSON.stringify(this.consulta_list)))
				}
			)
        },
        deleteConsulta:function(pk){
            console.log("Eliminar",pk)
            var url = URLS.endpoints.DetalleConsulta(pk);
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
		editConsultas:function(pk){
            console.log("editarConsulta", pk )
            var self = this;
			var url = URLS.endpoints.DetalleConsulta(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = self.makeFormDataConsulta(self.consulta);
			
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizara los datos de la Consulta.",
				icon: "warning",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, actualizar",
				cancelButtonText: "No, cancelar",
				customClass: {
					confirmButton: "btn font-weight-bold btn-success",
					cancelButton: "btn font-weight-bold btn-default"
				}
			})
        },
        makeFormDataConsulta: function(data_input){
			var data = new FormData();
			if (!!data_input.persona){
				data.append("persona", data_input.persona);
			}
			if (!!data_input.codigo_usuario){
				data.append("codigo_usuario", data_input.codigo_usuario);
			} 
			if (!!data_input.resultado){
				data.append("resultado", data_input.resultado);
			}
            if (!!data_input.observaciones){
				data.append("observaciones", data_input.observaciones);
			}
			if (!!data_input.infocred){
				data.append("infocred", data_input.infocred);
			}
			if (!!this.$refs.avatarFile.files.length > 0){
				//console.log("comprobante:",  this.$refs.avatarFile.files);
				data.append("infocred", this.$refs.avatarFile.files[0]);
			}else{
				console.log("notiene infocred");
			}
			
			return data
		},
		editarPersona: function(pk){
			console.log("Editar", pk)
		}
		
    },
    mounted: function(){
		
    }

})