var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
var CERTIFICADO_EDIT = {
	'codigo': null,
	'nombre': null,
	'fecha_vencimiento': null,
	'deudas_directas': null,
	'saldo_deudas_directas': null,
	'estado_deudas_directas': null,
	'deudas_indirectas': null,
	'saldo_deudas_indirectas': null,
	'estado_deudas_indirectas': null,
	'documento_identidad': null,
	'cite': null,
	'fecha_emision': null,
	'comentario_adicional': null,
	'estado': null,
	cliente: {
		'nombre': null,
		'deudas_directas': null,
		'dni': null,
		'saldo_deudas_directas': null,
		'deudas_indirectas': null,
		'saldo_deudas_indirectas': null,
	}
};
var CERTIFICADO = {
	'codigo': null,
	'nombre': null,
	'fecha_vencimiento': null,
	'deudas_directas': null,
	'saldo_deudas_directas': null,
	'estado_deudas_directas': null,
	'deudas_indirectas': null,
	'saldo_deudas_indirectas': null,
	'estado_deudas_indirectas': null,
	'documento_identidad': null,
	'cite': null,
	//'fecha_emision': getDateFormat(new Date()),
	'fecha_emision': null,
	'comentario_adicional': null,
	'estado': "V",
	'genero': 'H',
	'fecha_ultimo_pago':null,
};

function getDateFormat(d) {
	var anio = d.getFullYear();
	var mes = d.getMonth() + 1;
	var dia = d.getDate();
	return anio + "-" + mes + "-" + dia;
}
Date.prototype.addDays = function (d) { return new Date(this.valueOf() + 864E5 * d); };
var app = new Vue({
	el: "#kt_content_certificado",
	data: {
		certificados: null,
		level: false,
		certificadoError: null,
		certificado: CERTIFICADO,
		cliente: {
				'nombre': "Nombre del cliente",
				'deudas_directas': 0,
				'dni': "Cedula de identidad",
				'saldo_deudas_directas': "0.00",
				'estado_deudas_directas': null,
				'deudas_indirectas': 0,
				'saldo_deudas_indirectas': "0.00",
				'estado_deudas_indirectas': null,
				'genero': null,
				'titulo': null,
				'documento_identidad': null,
		},
		certificado_edit: {
				'codigo': null,
				'nombre': null,
				'fecha_vencimiento': null,
				'deudas_directas': null,
				'saldo_deudas_directas': null,
				'estado_deudas_directas': null,
				'deudas_indirectas': null,
				'saldo_deudas_indirectas': null,
				'estado_deudas_indirectas': null,
				'documento_identidad': null,
				'cite': null,
				'fecha_emision': null,
				'comentario_adicional': null,
				'estado': null,
				'slug': null,
				'fecha_ultimo_pago':null,
		},
		//editModal: null,
		modal: {
				editarCertificado: null,
		},
		is_vigente: false,
		next: null,
		previous: null,
		list: true,
		loader: false,
		access: null,
		ci_find: null,
		quien_firma: null,
		cargo_firma: null,
		certificado_errors: [],
	},
	computed: {
		indirectas: function(){
			return NumLetras(INDIRECTO);
		},
		deuda_indirectas: function(){
			return NumerosaLetras(MONTO_INDIRECTO);
		},
		deuda_directas: function(){
			return NumerosaLetras(MONTO_DIRECTO);
		},
		directas: function(){
			return NumLetras(DIRECTO);
		},
		estado_deuda_directa: function(){
			if(this.cliente.estado_deudas_directas=='V'){

				if(this.cliente.deudas_directas>1){
					return "Vigentes"
				}
				else{
					return "Vigente"
				}
			}
			if(this.cliente.estado_deudas_directas=='I'){
				return "Sin deuda"
			}
			if(this.cliente.estado_deudas_directas=='M'){
				return "En mora"
			}
			if(this.cliente.estado_deudas_directas=='S'){
					return "En castigo"
			}
		},
		estado_deuda_indirecta: function(){
			if(this.cliente.estado_deudas_indirectas=='V'){

				if(this.cliente.deudas_indirectas>1){
					return "Vigentes"
				}
				else{
					return "Vigente"
				}
			}
			if(this.cliente.estado_deudas_indirectas=='M'){
				return "En mora"
			}
			if(this.cliente.estado_deudas_indirectas=='S'){
					return "En castigo"
			}
		},
	},
	methods: {
		resetCertificado: function () {
			this.certificado = {
				'codigo': null,
				'nombre': null,
				'fecha_vencimiento': null,
				'deudas_directas': null,
				'saldo_deudas_directas': null,
				'estado_deudas_directas': null,
				'deudas_indirectas': null,
				'saldo_deudas_indirectas': null,
				'estado_deudas_indirectas': null,
				'documento_identidad': null,
				'cite': null,
				'fecha_emision': null,
				'comentario_adicional': null,
				'estado': null,
				'slug': null,
			};
		},

		addNewCertificado: function () {
			// create new certificado
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			//var data = new FormData();
			//var data = this.makeCertificadoData();  //estos son los datos a almacenar
			var url = URLS.endpoints.certifAdd(); //agara un url donde se mandan los datos para almacenar
			var data = this.certificado;

			//this.resetErrors();
			this.$http.post(url, data, _header).then(
				function (response) {
					this.certificado = response.body;
					toastr.success("El Certificado se ha almacenado correctamente", "<h6>Almacenado correctamente</h6>");
					window.location.href = URL_LIST;

				},
				function (responseError) {
					console.log("ERROR");
					this.errorCertificado = responseError.body;
					console.log(responseError);
				}
			);
		},
		verificateVigencia: function (date) {
			var vencimiento = new Date(date)
			var now = new Date;
			if (now.getTime() < vencimiento.getTime()) {
				this.is_vigente = true;
			} else {
				this.is_vigente = false;
			}
		},
		getCertificado: function (pk) {
			var url = URLS.endpoints.getCertificado(pk);
			//console.log(url);
			this.certificado_edit = CERTIFICADO_EDIT;
			this.certificado = CERTIFICADO_EDIT;

			this.$http.get(url).then(function (response) {
				this.certificado_edit = response.body
				this.certificado = response.body
				this.cliente = response.body
				this.verificateVigencia(this.certificado_edit.fecha_vencimiento);
				//console.log("Retornando certificado: ", this.certificado_edit);
				//this.modal.editarCertificado.modal('show');

			}, function (responseError) {
				console.log(responseError)
			});
		},
		getAccess: function () {
			var url = URLS.endpoints.getAccess();
						var self = this;
			this.$http.get(url).then(function (response) {
							self.access = response.body;
			}, function (responseError) {
							self.access = null;
				console.log(responseError)
			});
		},

		makeCertificadoData: function () {
			var data = new FormData();

			if (!!this.certificado.codigo) {
				data.append("codigo", this.certificado.codigo);
			}
			if (!!this.certificado.nombre_completo) {
				data.append("nombre", this.certificado.nombre_completo);
			}
			if (!!this.certificado.fecha_emision) {
				data.append("fecha_emision", this.certificado.fecha_emision);
				
				if (!!this.certificado.fecha_vencimiento) {
					data.append("fecha_vencimiento", this.getVencimiento(this.certificado.fecha_emision));
				}
			}
			if (!!this.certificado.deudas_directas) {
				data.append("deudas_directas", this.certificado.deudas_directas);
			}
			if (!!this.certificado.saldo_deudas_directas) {
				data.append("saldo_deudas_directas", this.certificado.saldo_deudas_directas);
			}
			if (!!this.certificado.estado_deudas_directas) {
				data.append("saldo_deudas_directas", this.certificado.estado_deudas_directas);
			}
			if (!!this.certificado.deudas_indirectas) {
				data.append("deudas_indirectas", this.certificado.deudas_indirectas);
			}
			if (!!this.certificado.saldo_deudas_indirectas) {
				data.append("saldo_deudas_indirectas", this.certificado.saldo_deudas_indirectas);
			}
			if (!!this.certificado.estado_deudas_indirectas) {
				data.append("saldo_deudas_indirectas", this.certificado.estado_deudas_indirectas);
			}
			if (!!this.certificado.documento_identidad) {
				data.append("documento_identidad", this.certificado.documento_identidad);
			}
			if (!!this.certificado.genero) {
				data.append("genero", this.certificado.genero);
				console.log("dato_genero******",this.certificado.genero);
			}
			if (!!this.certificado.cite) {
				data.append("cite", this.certificado.cite);
			}
			if (!!this.certificado.comentario_adicional) {
				data.append("comentario_adicional", this.certificado.comentario_adicional);
			}
			if (!!this.certificado.slug) {
				data.append("slug", this.certificado.slug);
			}
			if (!!this.certificado.fecha_ultimo_pago) {
				data.append("fecha_ultimo_pago", this.certificado.fecha_ultimo_pago);
			}

			return data;
		},

		loadCliente: function () {
      /**
       * esta funcion busca los datos del cliente
       */
      if (!!this.ci_find) {
				if(this.ci_find.indexOf("-")!=-1){
					this.ci_find = "'"+this.ci_find+"'";
				}

        var url = URLS.endpoints.getClienteCertificado(this.ci_find);
        this.loader = true;
        var acceso = {
          headers: {
            'Authorization': 'Bearer '+ this.access
          }
        };
        this.$http.get(url, acceso, { timeout: 5000 }).then(
          function (response) {
						console.log(response.body);
            this.loader = true;
						
            this.setCertificado(response.body.data);
						if(!!response.body.data[0].codigo_cliente){
							toastr.success("El cliente se ha cargado correctamente", "<h6>Cliente encontrado</h6>");
						}
						else{
            	toastr.error("El cliente no existe", "<h6>No se encontró</h6>");
						}
          },
          function (responseError) {
						console.log("Cliente NO encontrado", responseError);
            toastr.error("El cliente no existe", "<h6>No se encontró</h6>");
          }
        ).catch(function (response) {
            // can't catch timeout
            console.log("CATCH", response);
        })
        .finally(function () {
            //console.log("FINALLY");
            this.loader = false;
        });
      } else {
          toastr.error("Ingrese el numero de CI primero", "Error!");
      }
		},
		setCertificado: function(data){

			this.certificado.deudas_directas = data[0].deudas_directas;
			this.certificado.saldo_deudas_directas = data[0].saldo_deudas_directas;
			this.certificado.estado_deudas_directas = data[0].estado_deudas_directas;
			this.certificado.deudas_indirectas = data[0].deudas_indirectas;
			this.certificado.saldo_deudas_indirectas = data[0].saldo_deudas_indirectas;
			this.certificado.estado_deudas_indirectas = data[0].estado_deudas_indirectas;
			this.certificado.nombre = data[0].nombre_completo;
			this.certificado.documento_identidad = data[0].documento_identidad;
			this.certificado.fecha_ultimo_pago = data[0].fecha_ultimo_pago;
			this.certificado.codigo = data[0].codigo_cliente;
			//this.certificado.documento_identidad = data[0].ci;

			this.cliente.deudas_directas = data[0].deudas_directas;
			this.cliente.saldo_deudas_directas = data[0].saldo_deudas_directas;
			this.cliente.estado_deudas_directas = data[0].estado_deudas_directas;
			this.cliente.deudas_indirectas = data[0].deudas_indirectas;
			this.cliente.saldo_deudas_indirectas = data[0].saldo_deudas_indirectas;
			this.cliente.estado_deudas_indirectas = data[0].estado_deudas_indirectas;
			this.cliente.nombre_completo = data[0].nombre_completo;
			this.cliente.documento_identidad = data[0].documento_identidad;
			
			this.cliente.titulo = data[0].genero;
			if (this.cliente.titulo == 'F') {
					this.cliente.genero = 'M';
					this.certificado.genero = 'M'

			} else if (this.cliente.titulo == 'M') {
					this.cliente.genero = 'H';
					this.certificado.genero = 'H'
			}

		},
		getVencimiento: function (date) {
			var emision = new Date(date)
			return getDateFormat(emision.addDays(90));
		},

		saveCertificado: function (pk) {
			var self = this;
			var msg = "";
			if (!!this.certificado.cite) {
				msg = "Se almacenaran los datos.";
			}else{
				msg = "Falta el campo CITE, está seguro de continuar?";
			}
			Swal.fire({
				title: "¿Está seguro?",
				text: msg,
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
					var url = URLS.endpoints.postCertificado();

					self.certificado.fecha_vencimiento = self.getVencimiento(self.certificado.fecha_emision);
					//if (self.validarCite(self.certificado.cite))
					var data = self.certificado;
					/*
					if (data.genero == 'F') {
							data.genero = 'M';
					} else {
							data.genero = 'H';
<<<<<<< HEAD
					}*/
					// TODO: Mejorar manejo de fechas
					var today = new Date();
					var dd = today.getDate();
					var mm = today.getMonth()+1; 
					var yyyy = today.getFullYear();

					data['fecha_emision'] = yyyy+'-'+mm+'-'+dd;
					
					var vencimiento = new Date();
					ven = vencimiento.setDate(vencimiento.getDate() + 90);
					ven = new Date(ven);
					var dd_v = ven.getDate();
					var mm_v = ven.getMonth()+1; 
					var yyyy_v = ven.getFullYear();

					data['fecha_vencimiento'] = yyyy_v+'-'+mm_v+'-'+dd_v;

					self.$http.post(url, data, csrf_token).then(
						function (response) {
							toastr.success("El certificado se ha almacenado correctamente", "<h6>Almacenado correctamente</h6>");
							window.location.href = URL_LIST;
							//this.loadListCertificados();
=======
					}
					console.log("DATA:", data);
 					*/
					self.$http.post(url, data, csrf_token).then(
						function (response) {
							toastr.success("El certificado se ha almacenado correctamente", "<h6>Almacenado correctamente</h6>");
							window.location.href = URL_LIST;
							this.loadListCertificados();
>>>>>>> ruddy
						},
						function (responseError) {
							this.certificado_errors = responseError.body;
							console.log(this.certificado_errors)
						});
					}
			});
		},

		deleteCertificado: function (pk) {
			var url = URLS.endpoints.deleteCertificado(pk);
			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se eliminara el certificado y todos sus datos.",
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
		saveEditCertificado: function (pk) {
			var url = URLS.endpoints.editCertificado(pk);
			//console.log("Guardando certificado editado",url);

			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = this.certificado;
			console.log("data", data)
			this.$http.put(url, data, _header).then(function (response) {
				toastr.success("El certificado se ha actualizado correctamente", "<h6>Actualizacion correcta</h6>");
				this.modal.editarCertificado.modal('hide');
				//this.loadListCertificado();
			}, function (responseError) {
				console.log("Error al enviar actualizacion")
				//console.log(responseError.body)
			});
		},
		preSaveEditCertificado: function (pk) {
			var url = URLS.endpoints.editCertificado(pk);
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizaran los datos del certificado.",
				icon: "warning",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, actualizar!",
				cancelButtonText: "No, cancelar",
				customClass: {
					confirmButton: "btn font-weight-bold btn-success",
					cancelButton: "btn font-weight-bold btn-default"
				}
			}).then(function (result) {
				self.saveEditCertificado(pk)
			});


		},
		openEditModal: function (pk) {
			//console.log("abriendo modal para editar un certificado: ", pk);
			this.getCertificado(pk)
			this.modal.editarCertificado.modal('show');
		},
		closeEditCertificadoModal: function () {
			this.modal.editarCertificado.modal('hide');
		},
		printCertificado: function (){
			print();
		},
		toggleFirma: function(key){
			if (key=="CMAM"){
				this.quien_firma = "Lic. Carlos M. Alarcón Montes"
				this.cargo_firma = "Gerente General"
			}else{
				this.quien_firma = "Ing. Guillermo J. Burnett Mancilla"
				this.cargo_firma = "Gerente Operativo"
			}
		},
		
	},
	mounted: function () {
		this.getAccess()
		this.modal.editarCertificado = $(this.$refs.editModalCertificado);
		this.toggleFirma("CMAM");
		console.log("Cargando certificados")
	},

})