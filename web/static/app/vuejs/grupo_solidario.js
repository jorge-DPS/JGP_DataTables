var csrf_token = { headers: { "X-CSRFToken": csrftoken } };

var app = new Vue({
    el:'#formGrupo',
    delimiters: ['[[',']]'],
    data:{
        grupo:{
            'descripcion_grupo':null,
        },
        'grupo_edit':null,
        'lista_grupo': null,
        'error_grupo':[],
    },

    methods:{

        cargarGrupos: function () {
            console.log("entrando al metodo crear");
            var url = URLS.endpoints.craarListarGrupoSolidario();
            this.$http.get(url).then((response) => {
                this.lista_grupo = response.body;
                console.log(this.lista_zonas);
            });
        },

        createGrupoSolidario: function () {
            if (!!this.grupo.descripcion_grupo) {
                
                console.log("ingresa al metodo crear");
                var self=this;     
                Swal.fire({
                    title: "¿Está seguro?",
                    icon: "warning",
                    showCancelButton: true,
                    buttonsStyling: false,
                    confirmButtonText: "Si, enviar Grupo solidario!",
                    cancelButtonText: "No, cancelar",
                    customClass: {
                        confirmButton: "btn font-weight-bold btn-success",
                        cancelButton: "btn font-weight-bold btn-default"
                    }  
                }).then(function (result) {
                    if (result.value) {
                        var url = URLS.endpoints.craarListarGrupoSolidario();
                        console.log(this.grupo)
                        //var data = self.hacerFormDataZona(self.zona)
                        self.$http.post(url, self.grupo, csrf_token ).then(
                            function (response) {
                            toastr.success("Grupo solidario se ha almacenado correctamente", response.data);
                            window.location.href = URL_LIST;
                        },
                        function(responseError){
                            /* this.personas_erros = responseError.body
                            console.log(this.personas_erros) */
                            this.error_grupo = responseError.data
                            toastr.error("ERROR: AL ENVIAR LOS DATOS", responseError.body)
                            }
                        )
                        
                    }
                })
            }else{
                toastr.error("ERROR: AL ENVIAR LOS DATOS PORFAVOR REVISE LOS CAMPOS REQUERIDOS")

            }
        },

        getGrupoSolidario: function (pk) {
            var url = URLS.endpoints.editGrupoSolidario(pk);
            this.$http.get(url).then(
                function (response){
                    this.grupo = response.body;
                    console.log(this.grupo);
                }
            )
        },

        editarGrupoSolisario:function (pk) {
            if (!!this.grupo.descripcion_grupo) {
                console.log("========= EDITAR GRUPO SOLIDARIO =========");
                var self = this;
                var url = URLS.endpoints.editGrupoSolidario(pk)
                //var data = self.makeFormDataPersona(self.persona);
                
                Swal.fire({
                    title: "¿Está seguro?",
                    text: "Se actualizara los datos de Grupo.",
                    icon: "warning",
                    showCancelButton: true,
                    buttonsStyling: false,
                    confirmButtonText: "Si, actualizar",
                    cancelButtonText: "No, cancelar",
                    customClass: {
                        confirmButton: "btn font-weight-bold btn-success",
                        cancelButton: "btn font-weight-bold btn-default"
                    }
                }).then(function (result) {
                    if (result.value) {
                        console.log("========= EDITANDO GRUPO ===========", this.grupo);
                        self.$http.put(url, self.grupo, csrf_token).then(
                        //var _header = { headers: { "X-CSRFToken": csrftoken } };
                        function (response) {
                                toastr.success("Se ha actualizado correctamente la grupo solidario", "<h6>Actualizacion correcto</h6>",response.data);
                                window.location.href = URL_LIST;
                            },
                            function(responseError) {
                                this.error_grupo = responseError.body
                                toastr.error("ERROR: YA EXISTE LA DESCRIPCION NO PUEDE REPETIRSE, INTENTE CON OTRA DESCRIPCION", responseError.body)
                                
                            }
                        )
                        
                    }
                })  
            }else{
                toastr.error("ERROR: Al enviar los datos porfavor revise los campos")

            }
        },
        deleteGrupoSolidario:function (pk) {
            console.log("delete",pk)
			var url = URLS.endpoints.deleteGrupoSolidario(pk);
            //var _header = { headers: { "X-CSRFToken": csrftoken } };
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se eliminara grupo solidario y todos sus datos.",
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
					self.$http.delete(url, csrf_token).then(
						function (response) {
							console.log("eliminado", response)
                            window.location.href = URL_LIST;
						},
						function (responseError) {

							console.log("ERROR eliminado")
						}
					);
					//window.location.href = URL_LIST;
				}
			});
        }
    }
})