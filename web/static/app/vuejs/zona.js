var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
var app = new Vue({
    el: "#formularioZonas",
    delimiters: ['[[',']]'],
    data: {
        zona: {
            descripcion: null,
            localidad: null,
        },
        zona_edit:null,
        lista_zonas:null,
        localidades:null,
        error_zona: [],
        valor: false,
        //lc:$("#select").data.search,
    },

    filters: {
        capitalizar: function (data) {
            capitalized = [];
            data.split(" ").forEach((word) => {
                capitalized.push(
                    word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
                );
            });
            return capitalized.join(" ");
        },
    },

    methods: {

        deleteZona: function(pk){
            console.log("delete",pk)
			var url = URLS.endpoints.deleteZona(pk);
            //var _header = { headers: { "X-CSRFToken": csrftoken } };
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se eliminara la Zona y todos sus datos.",
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
                            toastr.success("Zona se ha eliminado correctamente", response.data);
                            window.location.href = URL_LIST; 
						},
						function (responseError) {
                            this.error_zona = responseError.data
                            toastr.error("error al eliminar los datos" + responseError.data);
						}
					);
					//window.location.href = URL_LIST;
				}
			});
        },

        cargarZonas: function () {
            console.log("entrando al metodo");
            var url = URLS.endpoints.crearListarZona();
            this.$http.get(url).then((response) => {
                this.lista_zonas = response.body;
                console.log(this.lista_zonas);
            });
        },

        
        cargarLocalidad: function () {
            console.log("entrando al metodo");
            var url = URLS.endpoints.crearListarLocalidad();
            this.$http.get(url).then((response) => {
                this.localidades = response.body;
                console.log(this.localidades);
            });
        },

        createZona:function () {
            //var _header = { headers: { "X-CSRFToken": csrftoken } };
            var self=this;     
            if (!!this.zona.descripcion && !!this.zona.localidad) {
                Swal.fire({
                    title: "¿Está seguro?",
                    icon: "warning",
                    showCancelButton: true,
                    buttonsStyling: false,
                    confirmButtonText: "Si, enviar Zona!",
                    cancelButtonText: "No, cancelar",
                    customClass: {
                        confirmButton: "btn font-weight-bold btn-success",
                        cancelButton: "btn font-weight-bold btn-default"
                    }  
                }).then(function (resultado) {
                    if (resultado.value) {
                        var url = URLS.endpoints.crearListarZona()
                        //console.log("aqui esta id", this.zona.localidad);
                        self.$http.post(url, self.zona, csrf_token ).then(
                            function (response) {
                                toastr.success("Zona se ha almacenado correctamente", response.data);
                                window.location.href = URL_LIST;   
                            },
    
                            //atrapando los errores desde el backend
                            function (responseError) {
                                this.error_zona = responseError.data
                                toastr.error("error al almacenar los datos" + responseError.data);
                                
    
                            }
                        )
                        
                    }
                })
                
            }else{
                // Define form element
            const form = document.getElementById('kt_docs_formvalidation_text');

            // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
            var validator = FormValidation.formValidation(
                form,
                {
                    fields: {
                        'text_input': {
                            validators: {
                                notEmpty: {
                                    message: 'Este campo "Descripcion Zonas" es requerido'
                                }
                            }
                        },
                        'select2_input': {
                            validators: {
                                notEmpty: {
                                    message: 'Este campo "Localidad" es requerido'
                                }
                            }
                        },
                    },

                    plugins: {
                        trigger: new FormValidation.plugins.Trigger(),
                        bootstrap: new FormValidation.plugins.Bootstrap5({
                            rowSelector: '.fv-row',
                            eleInvalidClass: '',
                            eleValidClass: ''
                        })
                    }
                }
            );
                toastr.error("error al almacenar los datos");
            }
                
        },

        getZona:function(pk){
            var url = URLS.endpoints.editZona(pk);
            this.$http.get(url ).then(
                function (response){
                    this.zona = response.body;
                    console.log(this.zona);
                }
            )
        },

        hacerMakeFormZona:function (data_input) {
            var data = new FormData();
            if (!!data_input.descripcion) {
               data.append('decripcion', data_input.descripcion) 
            }

            if (!!data_input.localidad) {
                data.append('localidad', data_input.localidad)
            }
            return data
        },

       editarZona: function (pk) {
        if (!!this.zona.descripcion && !!this.zona.localidad) {
            console.log("========= EDITAR ZONA =========");
            var self = this;
            var url = URLS.endpoints.editZona(pk)
            Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizara los datos de Zona.",
				icon: "warning",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, actualizar",
				cancelButtonText: "No, cancelar",
				customClass: {
					confirmButton: "btn font-weight-bold btn-success",
					cancelButton: "btn font-weight-bold btn-default"
				}
			}).then(function (resultado) {
                if (resultado.value) {
                    console.log("========= EDITANDO ZONA ===========", this.zona);
                    self.$http.put(url, self.zona, csrf_token).then(
                        function (response) {
                            toastr.success("Zona se ha Editado correctamente", response.data);
                            window.location.href = URL_LIST;   
                        },
                        function (responseError) {
                            error_zona = responseError.body
                            toastr.error("No se ha almacenado correctamente la zona" + responseError.data);

                        }
                    )
                    
                }
            })
            
        }else{
            if (this.zona.localidad != "") {
                
            }
            toastr.error("Zona no se ah llenado correctamente");

        }
            
			//var _header = { headers: { "X-CSRFToken": csrftoken } };
       },
        
    

        getLocalidad:function () {
            
        }
        
        /* pruebaFuncion: function ( ) {
            console.log("test==========================", "6");
        }, */

        
    },

    created: function () {
        this.cargarZonas();
        this.cargarLocalidad();
        
    },
});
