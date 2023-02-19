var CSFR_TOKEN = { headers: { "X-CSRFToken": csrftoken } };

var app = new Vue({
	el: "#kt_content_solicitud",
	data: {
		enlace_formulario: null,
		solicitud: {
			nombres: null,
			apellido_paterno: null,
			apellido_materno: null,
			numero_documento: null, 
			extension_documento: null,
			complemento_documento: null,
			whatsapp: null,
			monto_solicitado: null,
			monto_sugerido: null,
			plazo_meses: null,
			plazo_aniois: null,
			ingreso: null,
			destino: null,
			detalle_destino: null,
			fecha_solicitud: null,
			fecha_revision: null,
			slug: null,
			tipo_domicilio: null,
			estado_solicitud: null,
			comentario_revision: null,
			sucursal_cercano: null,
		},
		form_solicitud: {
			monto_sugerido: null,
			destino: null,
			estado: null,
			comentario_revision: null,
		},
		complemento: null,
		documentos: null,
		asesor_asignado: null,
		modal: {
			editarSolicitud: null,
			modalEnlaceFormulario: null,
			ubicacionSucursal: null,
			asignar_usuario: null,
		},
		users: null,
	},
	computed: {
		urlFoto: function () {
			return this.documentos.foto;
		},
		destino: function () {
			if (this.solicitud.destino == 'CO') {
				return "Capital operativo";
			} else if(this.solicitud.destino == 'CI') {
				return "Capital para inversión";
			} else if (this.solicitud.destino == 'BI') {
				return "Bienes";
			} else if (this.solicitud.destino == 'CON') {
				return "Consumo";
			} else if (this.solicitud.destino == 'TR') {
				return "Terreno";
			} else if (this.solicitud.destino == 'CONS') {
				return "Construcción";
			} else if (this.solicitud.destino == 'RE') {
				return "Refacciones";
			} else if (this.solicitud.destino == 'AN') {
				return "Anticretico";
			} else if (this.solicitud.destino == 'OT') {
				return "Otros";
			}
		},
		domicilio: function(){
			if (this.solicitud.tipo_domicilio == 'PRO') {
				return "Propio";
			} else if (this.solicitud.tipo_domicilio== 'ALQ'){
				return "Alquilado";
			} else if (this.solicitud.tipo_domicilio== 'ANT'){
				return "Anticrético";
			} else if (this.solicitud.tipo_domicilio== 'PRE'){
				return "Prestado";
			} else if (this.solicitud.tipo_domicilio== 'FAM'){
				return "De un familiar";
			} else if (this.solicitud.tipo_domicilio== 'OTR'){
				return "Otros";

			}

		},
		edad: function () {
			var today = new Date();
			var birthDate = new Date(this.complemento.fecha_nacimiento);
			var age = today.getFullYear() - birthDate.getFullYear();
			var m = today.getMonth() - birthDate.getMonth();
			if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
				age--;
			}
			return age + " años";
		},
		tipo_actividad: function () {
			return this.formatActividad(this.complemento.actividad_principal.tipo_actividad);
		},
		tipo_actividad_secundaria: function () {
			return this.formatActividad(this.complemento.actividad_secundaria.tipo_actividad);
		},
		tipo_ingreso: function () {
			return this.formatIngreso(this.complemento.actividad_principal.tipo_ingreso);
		},
		tipo_ingreso_secundaria: function () {
			return this.formatIngreso(this.complemento.actividad_secundaria.tipo_ingreso);
		},
		tenencia: function () {
			return this.formatTenencia(this.complemento.actividad_principal.tipo_tenencia);
		},
		tenencia_secundaria: function () {
			return this.formatTenencia(this.complemento.actividad_secundaria.tipo_tenencia);
		},
	},
	methods: {
		formatActividad: function (value) {
			if (value == 'F') {
				return "Fijo";
			} else if (value == 'B') {
				return "Ambulante";
			} 
		},
		formatIngreso: function (value) {
			if ( value == 'D') {
				return "Dependiente";
			} else if ( value == 'I') {
				return "Independiente";
			} 
		},
		formatTenencia: function (value) {
			if (value == 'A') {
				return "Alquilado";
			} else if (value == 'E') {
				return "Expropiado";
			} else if (value == 'F') {
				return "De un familiar";
			} else if (value == 'N') {
				return "Financiada / pagando aun";
			} else if (value == 'P') {
				return "Propio";
			} else if (value == 'R') {
				return "Portero / cuidador";
			} else if (value == 'S') {
				return "Prestado";
			} else if (value == 'T') {
				return "Anticrético";
			} else if (value == 'O') {
				return "Otros";
			} 
		},
		getSolicitud: function(slug) {
			//console.log("cargando certificado: ", slug);
			var url = URLS.endpoints.getSolicitud(slug);
			
			this.$http.get(url).then(function(response) {
				//console.log("Retornando solicitud: ", response.body);
				this.solicitud = response.body.solicitud;
				this.complemento = response.body.complemento;
				this.documentos = response.body.documentos;
				this.asesor_asignado = response.body.asesor_asignado;

				this.form_solicitud.destino = this.solicitud.destino;
				this.form_solicitud.estado_solicitud = this.solicitud.estado_solicitud;
				this.form_solicitud.comentario_revision = this.solicitud.comentario_revision;
				this.form_solicitud.monto_sugerido = this.solicitud.monto_sugerido;
				//this.modal.editarCertificado.modal('show');

			}, function(responseError) {
				console.log(responseError)
			});
		},
		/*
		openEditModalSolicitud: function(slug) {
			this.getSolicitud(slug)
			this.modal.editarSolicitud.modal('show');
		},
		*/
		updateSolicitud: function (slug) {
			var url = URLS.endpoints.updateSolicitud(slug);
			var data = this.form_solicitud;
			data.usuario= USER;
			//console.log("Eliminando solicitud", _header);
			
			this.$http.put(url, data, CSFR_TOKEN).then(
				function(response){
					//console.log("eliminado!!!" , URL_LIST);
					this.solicitud_success = response.body;
					toastr.success("Datos actualizados", "<h6>Almacenado correctamente</h6>");
					//window.location.href = URL_LIST;
				},
				function(errorResponse){
					//console.log("Creando!!!" , errorrResponse);
					toastr.error("Datos actualizados", "<h6>Error al almacenar</h6>");
					this.success = false;
				},
			);
		},
		cleanFormSolicitud: function () {
			this.form_solicitud = {
				destino: null,
				estado_solicitud: null,
				comentario_revision: null,
				monto_sugerido: null,
			}
		},
		deleteSolicitud: function (slug) {
			var url = URLS.endpoints.deleteSolicitud(slug);
            var _header = CSFR_TOKEN;
			var data = {'estado_solicitud':'EL'};
			//console.log("Eliminando solicitud", _header);
			
			this.$http.put(url, data, _header).then(
				function(response){
					//console.log("eliminado!!!" , URL_LIST);
					this.solicitud_success = response.body;
					window.location.href = URL_LIST;
				},
				function(errorResponse){
					//console.log("Creando!!!" , errorrResponse);
					this.success = false;
				},
			);
		},

		closeModal: function(){
			this.modal.editarSolicitud.modal('hide'); 
		},
		openEnlaceFormularioModal: function (slug) {
			//console.log("abriendo modal para mostrar enlace: ", slug);
			this.generarFormularioComplemento(slug);
			this.modal.modalEnlaceFormulario.modal('show');
		},
		closeEnlaceFormularioModal: function () {
			//console.log("abriendo modal para editar un certificado: ", slug);
			this.modal.modalEnlaceFormulario.modal('hide');
		},
		generarFormularioComplemento: function (slug) {
			var url = URLS.endpoints.urlFormularioComplemento(slug);
			//console.log("Generando enlace", url)
			this.enlace_formulario =  url;
			//https://api.whatsapp.com/send?phone=76543210&text=*Tu%20solicitud%20fue%20aprobada*,%20por%20favor%20llena%20el%20siguiente%20formulario:%20url
		},
		openWhatsappMessage: function (slug, nombre, numero) {
			this.generarFormularioComplemento(slug);
			var url_whatsapp = "https://wa.me/%2B591"+numero+"?"
				+ "text=Estimad@%20" + nombre
				+ "%20*¡Tu%20solicitud%20ha%20sido%20revisado!*,"
				+ "%0APor%20favor%20ahora%20puedes%20llenar%20el%20siguiente%20formulario:%0A"
				+ this.enlace_formulario;
				//+ this.generarFormularioComplemento(slug);
			window.open(url_whatsapp, "_blank");
		},
		copyEnlaceFormulario: function (slug) {
			this.generarFormularioComplemento(slug);
			this.$copyText(this.enlace_formulario).then(function (e) {
				console.log('Copied', e)
				toastr.primary("Ahora puedes compartirlo con el cliente.", "<h6>Enlace copiado!!</h6>");
			}, function (e) {
				console.log('Can not copy', e)
			});
		},
		openWhatsapp: function (numero) {
			console.log('abriendo whatsapp');
			var url_whatsapp = "https://wa.me/%2B591" + numero;
				
			window.open(url_whatsapp, "_blank");
		},
		userAssigned: function(){
			this.modal.asignar_usuario.modal('show');
			this.loadUsers();
		},
		loadUsers:function(){
			let url = URLS.endpoints.getUsers();
			if (!this.users) {
				this.$http.get(url).then(function(response){
					console.log("cargando usuarios", response.body);
					if (!!response.body.results) {
						this.users = response.body.results;
					}else{
						this.users = response.body;
					}
				}, function(errorResponse){
					console.log("error al cargar usuarios", errorResponse);
				});
			}
		},
		toggleAssignAdviser:function (asesor){
			let data = {
				'asesor': asesor,
				'usuario': USER,
			}
			let url = URLS.endpoints.assignAdviser(SLUG);
			//console.log("asignando usuario", data, url);
			this.$http.put(url, data, CSFR_TOKEN).then(
				function(response){
					//console.log("Asignando usuario", response.body);
					this.solicitud = response.body;
					this.modal.asignar_usuario.modal('hide');
					if(asesor=="null"){
						toastr.warning("Asesor desasignado", "<h6>Asesor desasignado</h6>");
					}else{
						toastr.success("Asesor asignado correctamente", "<h6>Asesor asignado!!</h6>");
					}
				}, function(errorResponse){
					console.log("Error al asignar usuario", errorResponse);
				}
			);
		},
	},
	mounted: function () {
    DatepickerSolicitud.init();
    
		if(!!SLUG){this.getSolicitud(SLUG);}
		
    this.modal.asignar_usuario = $(this.$refs.modalAsignarUsusario);
		this.modal.modalEnlaceFormulario = $(this.$refs.modalEnlaceFormulario);
    this.modal.editarSolicitud = $(this.$refs.editModalSolicitud);
		//console.log("Iniciando solicitudes", this.modal.editarSolicitud);
		//this.openEditModalSolicitud(SLUG);
		//this.userAssigned();
	},
})

