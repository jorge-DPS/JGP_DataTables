var CSFR_TOKEN = { headers: { "X-CSRFToken": csrftoken }, 'Content-Type': 'multipart/form-data' };

var SOLICITUD = {
	nombres: null,
	apellido_paterno: null,
	apellido_materno: null,
	numero_documento: null,
	extension_documento: null,
	complemento_documento: null,
	whatsapp: null,
	monto_solicitado: null,
	plazo: null,
	ingreso: null,
	destino: null,
	detalle_destino: null,
	fecha_solicitud: null,
	slug: null,
	estado_solicitud: null,
	actividad_economica: null,
	correo_electronico: null,
	sucursal_cercana: null,
	tipo_domicilio: null,
	forma_pago: "SEMANAL",
	tipo_ingreso: "I",
};
var SOLICITUD_DATOS = {
	nombres: "Jacinto",
	apellido_paterno: "Perez",
	apellido_materno: null,
	numero_documento: "8563214",
	extension_documento: null,
	complemento_documento: null,
	whatsapp: 78965410,
	monto_solicitado: 12000,
	plazo: 9,
	ingreso: 2500,
	destino: null,
	detalle_destino: "Compra de viveres para la pandemia",
	fecha_solicitud: null,
	slug: null,
	estado_solicitud: null,
	actividad_economica: "Negocio de reenes",
	forma_pago: "SEMANAL",
	correo_electronico: "cliente@mail.com",
	tipo_domicilio: null,
	tipo_ingreso: "I",
};
var SOLICITUD_COMPLEMENTO_DATOS = {
	documento: DOCUMENTO_SOLICITUD,
	nombres: null,
	nacionalidad: 'BO',
	dependientes: 0,
	genero: "M",
	lugar_nacimiento: "El Alto, La Paz",
	fecha_nacimiento: null,
	estado_civil: 'S',
	ciudad: null,
	zona_domicilio: null,
	direccion_domicilio: 'Calle 23, Nro, 6',
	referencia_domicilio: 'Al lado de la tienda de doña Maria',
	nombre_completo_referencia: 'Juan Valdez',
	telefono_referencia: '74563210',
	parentesco_referencia: 'Cuñado',
	direccion_referencia: 'Z. Velazco, av. Juancito pinto, Nro. 4',
	nombre_completo_referencia_actividad: 'Feddy Vega',
	telefono_referencia_actividad: '74125630',
	parentesco_referencia_actividad: 'Primo',
	direccion_referencia_actividad: 'Calacoto, calle 3, nro 6666',
	ubicacion_gps: null,
	nombres: 'Juan',
	apellido_paterno: 'Nieves',
	deudas: null,
};
var SOLICITUD_COMPLEMENTO = {
	documento: DOCUMENTO_SOLICITUD,
	nombres: null,
	nacionalidad: 'BO',
	dependientes: 0,
	genero: "M",
	lugar_nacimiento: null,
	fecha_nacimiento: null,
	estado_civil: null,
	ciudad: null,
	zona_domicilio: null,
	direccion_domicilio: null,
	referencia_domicilio: null,
	nombre_completo_referencia: null,
	telefono_referencia: null,
	parentesco_referencia: null,
	direccion_referencia: null,
	nombre_completo_referencia_actividad: null,
	telefono_referencia_actividad: null,
	parentesco_referencia_actividad: null,
	direccion_referencia_actividad: null,
	ubicacion_gps: null,
	nombres: null,
	apellido_paterno: null,
	deudas: null,
};
var MESES = {
	'1': 'Enero',
	'2': 'Febrero',
	'3': 'Marzo',
	'4': 'Abril',
	'5': 'Mayo',
	'6': 'Junio',
	'7': 'Julio',
	'8': 'Agosto',
	'9': 'Septiembre',
	'10': 'Octubre',
	'11': 'Noviembre',
	'12': 'Diciembre',
}
var ACTIVIDAD_DATOS = {
	documento: null,
	descripcion: 'Venta de verduras al por menor en mercado',
	anios_experiencia: 3,
	anios_negocio: 2,
	dias_laborales: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
	hora_inicio: null,
	hora_fin: null,
	tipo_tenencia: 'P',
	tipo_actividad: "F",
	tipo_ingreso: "D",
};
var ACTIVIDAD = {
	documento: null,
	descripcion: null,
	anios_experiencia: null,
	anios_negocio: null,
	dias_laborales: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
	hora_inicio: "8:00",
	hora_fin: "18:00",
	tipo_tenencia: null,
	tipo_actividad: "F",
	tipo_ingreso: "D",
};
var ACTIVIDAD_SECUNDARIA = {
	documento: null,
	descripcion: null,
	anios_experiencia: null,
	anios_negocio: null,
	direccion_actividad: null,
	dias_laborales: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
	hora_inicio: "8:00",
	hora_fin: "18:00",
	tenencia: null,
	tipo_actividad: "FIJO",
	tipo_ingreso: "DEPENDIENTE",
};
var DIRECCION_SECUNDARIA = {
	ciudad: null,
	zona: null, // esta es una Ubicacion
  calle_avenida: null,
  nombre_numero: null,	
};
var DIRECCION = {
	ciudad: null,
	zona: null, // esta es una Ubicacion
  calle_avenida: null,
  nombre_numero: null,	
};
var DIRECCION_DATOS = {
	ciudad: 'El Alto',
	zona: null, // esta es una Ubicacion
  calle_avenida: 'Calle 23',
	nombre_numero: 'Nro. 6',
};
var app = new Vue({
	el: "#kt_content_credito",
	data: {
		fecha: {
			dia: null,
			mes: null,
			año: null,
		},
		solicitud_success: false,
		solicitud: SOLICITUD,
		solicitud2: SOLICITUD_COMPLEMENTO,
		actividad_economica: ACTIVIDAD,
		direccion_actividad: DIRECCION,
		actividad_secundaria: null,
		direccion_actividad_secundaria: null,
		documentos: {
			documento: DOCUMENTO_SOLICITUD,
			foto: null,
			fotocopia_documento_identidad: null,
			foto_ci_anverso: null,
			foto_ci_reverso: null,
		},
		fotos_solicitud: {
			documento: null,
			foto: null,
			tipo_foto: null,
		},
		departamento: null,
		success: false,
		listaSolicitudes: null,
		modal: {
			editarSolicitud: null,
		},
		//ciudades:null,
		lista_ciudades:null,
		lista_zonas: null,
		whatsapp_state: null,
		celular_referencia_state: null,
		celular_referencia_actividad_state: null,
		actividad_secundaria_key: false,
		otras_deudas: false,
		foto_fotocopia: false,
		dz_domicilio: null,
		dz_negocio: null,
		dz_boleta: null,
		complemento: 'false',
		sucursales: null,
	},
	computed: {
		dias: function () {
			var array = [];
			for (i = 0; i < 31; i++){
				array[i] = i+1;
			}
			return array;
		},
		meses: function () {
			return MESES;
		},
		años: function () {
			var today = new Date();
			var year = today.getFullYear()-90;
			var array = [];
			
			for (i = 0; i <= 72; i++){
				array[i] = year;
				year++;
			}
			return array;
		},
	},
	watch: {
		'solicitud2.ciudad': function (newValue, oldValue ) {
			//console.log("Valores de ciudad", newValue);
			this.filterZonas(newValue);
		},
		'direccion_actividad.ciudad': function (newValue, oldValue ) {
			//console.log("Valores de ciudad", newValue);
			this.filterZonas(newValue);
		},
		'direccion_actividad_secundaria.ciudad': function (newValue, oldValue ) {
			//console.log("Valores de ciudad", newValue);
			this.filterZonas(newValue);
		},
		'solicitud.whatsapp'(newValue, oldValue) {
			this.whatsapp_state=this.validateCelular(newValue);
		},
		'solicitud2.telefono_referencia'(newValue, oldValue) {
			//console.log(newValue);
			this.celular_referencia_state=this.validateCelular(newValue);
		},
		'solicitud2.telefono_referencia_actividad'(newValue, oldValue) {
			//console.log(newValue);
			this.celular_referencia_actividad_state=this.validateCelular(newValue);
		},
	},
	methods: {
		toggleDeuda: function () {
			this.foto_fotocopia = this.foto_fotocopia ? false : true;
		},
		toggleDeuda: function () {
			this.otras_deudas = this.otras_deudas ? false : true;
		},
		toggleActividadSecundaria() {
			//console.log("Agregando actividad secundaria");
			this.actividad_secundaria = ACTIVIDAD_SECUNDARIA;
			this.direccion_actividad_secundaria = DIRECCION_SECUNDARIA;
			//this.actividad_secundaria.documento = DOCUMENTO_SOLICITUD;
			this.actividad_secundaria_key = this.actividad_secundaria_key ? false : true;
			this.getDepartamentoConection();
		},
		validateCelular(number) {
			if (number && number.length == 8) {
				if (number > 60000000 && number <= 79999999) {
					return false;
				} else { return true;}
			} else { return true; }
			
			//if (number.length == 0) { return null;}
		},
		listSolicitudes: function () {
			var url = URLS.endpoints.ListCreateCredito();
			//console.log("Cargando lista de solicitudes");
			
			this.$http.get(url).then(
				function(response){
					this.listaSolicitudes = response.body;
				},
			);
		},
		createSolicitud: function () {
			var url = URLS.endpoints.ListCreateCredito();
			var data = this.solicitud;
			
			this.$http.post(url, data, CSFR_TOKEN).then(
				function(response){
					//console.log("Creando!!!" , response);
					toastr.success("Su solicitud se ha enviado!!", "<h6>Solicitado</h6>");
					this.success = true;
					this.solicitud_success = response.body;
					this.solicitud = null;
				},
				function(errorResponse){
					console.log("Creando!!!" , errorrResponse);
					this.success = false;
				},
			);
		},
		createFotoSolicitud: function () {
			var url = URLS.endpoints.createSolicitudFotos();
			var _header = CSFR_TOKEN;
			var data = this.fotos_solicitud;
			//console.log("Creando nueva solicitud de fotos", data);
			
			this.$http.post(url, data, _header).then(
				function(response){
					//console.log("Creando!!!" , response);
					this.success = true;
					this.solicitud_success = response.body;
					this.solicitud = null;
				},
				function(errorResponse){
					//console.log("ERROR Creando!!!" , errorrResponse);
					this.success = false;
				},
			);
		},
		createSolicitudStep2: function () {
			var url_documentos = URLS.endpoints.createSolicitudDocumentos();
			var data_documentos = this.makeDataDocumentos();
			var self = this;
			var id_documentos = null;
			this.$http.post(url_documentos, data_documentos, CSFR_TOKEN).then(
				function (response) {
					//toastr.success("Documento Creando", "<h6>Almacenado</h6>");
					//console.log("Documento Creando!!!", response);
					var url = URLS.endpoints.createSolicitudComplemento(SLUG);
					id_documentos = response.body.id;
					var data = self.makeDataSolicitudComplemento(id_documentos)
					this.$http.post(url, data, CSFR_TOKEN).then(
						function (response) {
							toastr.success("Solicitud Complemento Creando", "<h6>Almacenado</h6>");
							this.success = true;
						},
						function (errorResponse) {
							//console.log("Error al crear solicitud complemento!!!", errorrResponse);
							this.success = false;
						},
					);
				},
				function (errorResponse) {
					this.success = false;
				},
			);			
		},

		makeDataSolicitudComplemento: function (id_documentos) {
			/** Creamos data para mandar y guardar - se genera de acuerdo a si tiene actividad secundaria */
			if (this.actividad_secundaria_key) {
				var data = {
					'data_documentos': id_documentos,
					'data_solicitud': this.solicitud2,
					'data_direccion_actividad': this.direccion_actividad,
					'data_actividad': this.actividad_economica,
					'data_direccion_actividad_secundaria': this.direccion_actividad_secundaria,
					'data_actividad_secundaria': this.actividad_economica,
				};
			} else {
				var data = {
					'data_documentos': id_documentos,
					'data_solicitud': this.solicitud2,
					'data_direccion_actividad': this.direccion_actividad,
					'data_actividad': this.actividad_economica,
					'data_direccion_actividad_secundaria': null,
					'data_actividad_secundaria': null,
				};
			}
			return data;
		},
    /*
    openEditModal: function(slug) {
			//console.log("abriendo modal para editar un certificado: ", slug);
			//this.getCertificado(pk)
			this.modal.editarCertificado.modal('show');
		},
    */
		getDepartamentoConection() {
			var url = "https://api.ipify.org?format=json";
			var url_city = "http://ip-api.com/json/"
			var self = this
			this.$http.get(url_city).then(
				function (res) {
					//console.log("Datos de ciudad", res.body)
					this.departamento = res.body.city;
					self.filterCiudades(this.departamento);
					
					KTBootstrapTimepickerSecundario.init();
				},
				function (errorResponse) {
					this.departamento = "La Paz";
					self.filterCiudades(this.departamento);
					//console.log(errorResponse.body);					
				}
			)
			/*
			this.$http.get(url).then(
				function (response) {
					var ip = response.body.ip
					//console.log("Ip obtenido", ip);
					self.$http.get(url_city).then(
						function (res) {
							self.departamento = res.body.city;
							console.log("Datos de ciudad",res.body.city)
						}
					)
				},
				function (errorResponse) {
					console.log("Ip NO obtenido", errorResponse)
					
				}
			)
			*/
		},
		filterCiudades: function(departamento) {
			var url = URLS.endpoints.ubicacionFilterCity();
			var data = { 'departamento': departamento };
            
			//console.log("CARGANDO CIUDADES", url, data);
			this.$http.put(url, data, CSFR_TOKEN).then(
				function (response) {
					//console.log("Cargando ciudades");
					const lista_ciudades = response.body.lista_ciudades;
					this.lista_ciudades = lista_ciudades;
					this.typeheadCitiesPrepare(lista_ciudades);
				},
				function (errorResponse) {
					console.log(errorResponse.body);					
				}
			);
		},
		typeheadCitiesPrepare: function (_ciudades) {
			/**
			 * Metodo para cargar el input de ciudades con el typehead
			 */
			var city = []
			for (item in _ciudades) {
				city.push(_ciudades[item][1]);
			}
			//console.log("------------------------->", city);
			TypeaheadCiudad.init(city);
			TypeaheadCiudadActividad.init(city);
			TypeaheadCiudadActividadSecundaria.init(city);
		},
		typeheadZonesPrepare: function (_zonas) {
			/**
			 * Metodo para cargar el input de zonas con el typehead
			 */
			var zone = []
			for (item in _zonas) {
				zone.push(_zonas[item].zona_urbanizacion);
			}
			
			TypeaheadZona.init(zone);
			TypeaheadZonaActividad.init(zone);
			TypeaheadZonaActividadSecundaria.init(zone);
		},

		filterZonas: function (ciudad) {
			var data = { 'codigo_ciudad': this.getCodigoCiudad(ciudad) };
			var url = URLS.endpoints.ubicacionFilterZone();
			//console.log("CARGANDO ZONAS", url, data);	
			this.$http.put(url, data, CSFR_TOKEN).then(
				function (response) {
					//console.log(response.body);
					const zonas = response.body;
					this.zonas = zonas;
					this.typeheadZonesPrepare(zonas);
				},
				function (responseError) {
					console.log("Error en filtrar zonas", responseError.body);
				}
			)
		},
		getCodigoCiudad: function (ciudad) {
			var ciudades = this.lista_ciudades;
			for (item in ciudades) {
				if (ciudades[item][1] == ciudad) {
					return ciudades[item][0];
				}
			}
			return null;
		},
		
		makeDataDocumentos: function (){
			//console.log("Data make for documents");
			var data = new FormData();

			data.append('documento', DOCUMENTO_SOLICITUD);
      if (this.$refs.fotoFile.files.length > 0){
        data.append('foto', this.$refs.fotoFile.files[0]);
			}
      if (this.$refs.fotocopiaFile.files.length > 0){
        data.append('fotocopia_documento_identidad', this.$refs.fotocopiaFile.files[0]);
			}
      if (this.$refs.ciAnversoFile.files.length > 0){
        data.append('foto_ci_anverso', this.$refs.ciAnversoFile.files[0]);
			}
      if (this.$refs.ciReversoFile.files.length > 0){
        data.append('foto_ci_reverso', this.$refs.ciReversoFile.files[0]);
			}
      if (this.$refs.luzFile.files.length > 0){
        data.append('factura_luz', this.$refs.luzFile.files[0]);
			}
      if (this.$refs.aguaFile.files.length > 0){
        data.append('factura_agua', this.$refs.aguaFile.files[0]);
			}
			
			//console.log("data",data);  
			return data;
		},
		dropzoneDomicilio: function () {
			var self = this;
			var url = "null"
			var id = parseInt(ID_SOLICITUD);
			var url = "/api/v1/solicitud/" + SLUG + "/fotos/";
			
			this.dz_domicilio.dropzone({
				url: url, // Set the url for your upload script location
				paramName: "foto	", // The name that will be used to transfer the file
				maxFiles: 5,
				maxFilesize: 10, // MB
				addRemoveLinks: true,
				//autoProcessQueue: false,
				headers: {
					"X-CSRFToken": csrftoken
				},
				acceptedFiles: "image/*,application/pdf,.psd",
				accept: function (file, done) {
					//console.log("ACEPT METHOD");
					done();
				},
				sending: function (file, xhr, formData) {
					//formData.append("filesize", file.size);
					formData.append("solicitud", id);
					formData.append("documento", DOCUMENTO_SOLICITUD);
					formData.append("tipo_foto", "DOMICILIO");
					//console.log(file.size);
				},
			});
		},
		dropzoneBoleta: function () {
			var self = this;
			var url = "/api/v1/solicitud/" + SLUG + "/fotos/";
			var id = parseInt(ID_SOLICITUD);
			this.dz_boleta.dropzone({
				url: url, // Set the url for your upload script location
				paramName: "foto	", // The name that will be used to transfer the file
				maxFiles: 5,
				maxFilesize: 10, // MB
				addRemoveLinks: true,
				//autoProcessQueue: false,
				headers: {
					"X-CSRFToken": csrftoken
				},
				acceptedFiles: "image/*,application/pdf,.psd",
				accept: function (file, done) {
					//console.log("ACEPT METHOD");
					done();
				},
				sending: function (file, xhr, formData) {
					//formData.append("filesize", file.size);
					formData.append("solicitud", id);
					formData.append("documento", DOCUMENTO_SOLICITUD);
					formData.append("tipo_foto", "BOLETA");
					//console.log(file.size);
				},
			});
		},
		dropzoneNegocio: function () {
			var self = this;
			var url = "/api/v1/solicitud/" + SLUG + "/fotos/";
			var id = parseInt(ID_SOLICITUD);
			this.dz_negocio.dropzone({
				url: url, // Set the url for your upload script location
				paramName: "foto	", // The name that will be used to transfer the file
				maxFiles: 5,
				maxFilesize: 10, // MB
				addRemoveLinks: true,
				//autoProcessQueue: false,
				headers: {
					"X-CSRFToken": csrftoken
				},
				acceptedFiles: "image/*,application/pdf,.psd",
				accept: function (file, done) {
					//console.log("ACEPT METHOD");
					done();
				},
				sending: function (file, xhr, formData) {
					//formData.append("filesize", file.size);
					formData.append("solicitud", id);
					formData.append("documento", DOCUMENTO_SOLICITUD);
					formData.append("tipo_foto", "ACTIVIDAD");
					//console.log(file.size);
				},
			});
		},
		getSucursales: function () {
			let url = URLS.endpoints.getSucursales();
			//console.log("url", url);
			this.$http.get(url).then(
				function (response) {
					//console.log("---->",response.body);
          if(!!response.body.results){
            this.sucursales = response.body.results;
          }else{            
            this.sucursales = response.body;
          }
          this.solicitud.sucursal_cercana = this.sucursales[0].slug;
				}, function (error) {
					console.log(error);
				});
		},
	},
	mounted: function () {
		this.listSolicitudes();
		this.getDepartamentoConection();
		KTBootstrapTimepicker.init();
		this.actividad_economica.documento = DOCUMENTO_SOLICITUD;
		//this.filterCiudades();
    //this.modal.editarSolicitud = $(this.$refs.editModalSolicitud);
    this.getSucursales();
    if (!!SLUG){
      this.dz_domicilio = $(this.$refs.dz_domicilio);
      this.dz_negocio = $(this.$refs.dz_negocio);
      this.dz_boleta = $(this.$refs.dz_boleta);
      this.dropzoneDomicilio();
      this.dropzoneNegocio();
      this.dropzoneBoleta();
    }
    
	},
	//updated: function () {
		//if (COMPLEMENTO != 'None') { this.success = true; }
	//},

})

/**
 * https://jesusfernandeztoledo.com/ejercicios-resueltos-arrays-en-javascript/
 * 
 * dado el siguiente array [63,45,58,56,45,58]
 * mostrar la suma de los elementos del array >> 325
 * mostrar el promedio >> 54.16
 * mostrar el elemento mayor >> 63
 * mostrar el elemento menor >> 45
 * eliminar los elementos repetidos >> [63,45,58,65]
 */

