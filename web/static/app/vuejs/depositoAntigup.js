var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
var DEPOSITO_1 = {
	'codigo_asesor':null,
	'prestamo': null,
	'codigo_cliente': null,
	'fecha': null,
	'banco': null,
	'importe': 0,
	'observaciones': null,
	'image': null,
	'estado': "SR",
};
var DEPOSITO_EDIT = {
	'codigo_asesor':null,
	'prestamo': null,
	'codigo_cliente': null,
	'fecha': null,
	'banco': null,
	'importe': 0,
	'observaciones': null,
	'image': null,
	'estado': "SR",

};
var app = new Vue({
	el: "#kt_content",
	data: {
		depositos: null,
		level: false,
		depositoError: null,
		deposito: {

			'codigo_asesor': null,
			'prestamo': "3216548",
			'codigo_cliente': null,
			'fecha': "2021-05-18",
			'banco': null,
			'importe': 0.12,
			'observaciones': null,
			'image': 'Remove photo',
			'estado': "SR",
		},
		bancos:null,
		deposito_edit: {
			'id':null,
			'codigo_asesor': null,
			'prestamo': null,
			'codigo_cliente': null,
			'fecha': null,
			'banco': null,
			'importe': 0,
			'observaciones': null,
			'image': null,
			'estado': null,
		},
		image_url:null,
		modal: {
			editarDeposito: null,

		},
	},

	methods: {
		doMath: function (index) {
			return index+1
		},
		openEditModal: function(pk) {
			console.log("abriendo modal para editar un deposito: ", pk);
			this.getDeposito(pk);
		},
		closeEditDepositoModal: function(){
			this.deposito_edit = DEPOSITO_EDIT;
			this.modal.editarDeposito.modal('hide');
			console.log("Clean Edit: ", this.deposito_edit )
		},
		saveEditDeposito: function(pk){
			var url = URLS.endpoints.getDeposito(pk);
			console.log("Guardando deposito editado",url);

			var _header = { headers: { "X-CSRFToken": csrftoken } };
			var data = this.makeDepositoData(this.deposito_edit);

				data.append("estado", this.deposito_edit.estado);

				console.log(data);

			this.$http.put(url, data, _header).then(function(response) {
				//this.modal.editarDeposito.modal('hide');
				this.loadListDepositos();
				toastr.success("El deposito se ha almacenado correctamente", "<h6>Almacenado correctamente</h6>");
				window.location.href = URL_LIST;
			}, function(responseError) {
				console.log(responseError.body)
			});
		},
		loadListDepositos: function() {
			console.log("Cargando Lista de DEPOSITOS");
			var url = URLS.endpoints.depos();
			this.$http.get(url).then(
				function(response) {
					this.depositos = response.body.result;
					console.log(response.body)
				},
				function(responseError) {
					console.log("ERROR");
					console.log(responseError);
				}
			);
		},

		resetErrors: function() {
			this.errorDeposito = {
				'asesor':[],
				'cliente': [],
				'prestamo': [],
				'fecha': [],
				'banco': [],
				'importe': [],
				'observaciones': [],
				'image': [],
				'estado': [],
			};
			this.error.asesor = false;
			this.error.cliente = false;
			this.error.prestamo = false;
			this.error.fecha = false;
			this.error.banco = false;
			this.error.importe = false;
			this.error.observaciones = false;
			this.error.image = false;
			this.error.estado = false;
		},
		resetDeposito: function() {
			this.deposito = {
				'asesor': null,
				'cliente': null,
				'prestamo': null,
				'fecha': null,
				'banco': null,
				'importe': null,
				'observaciones': null,
				'image': null,
				'estado': "SR",
			};
		},
		previewaddNewDeposito: function(){
			self = this;
			Swal.fire({
				title: 'Swal Title',
				text: 'Your swal text',
				type: 'warning',
				confirmButtonText: "Guardar",
				showCancelButton: true,
				cancelButtonText: 'cancel'
			 }).then(function(result){
				 //console.log(result)
				self.addNewDeposito();
				//console.log("se guardo!!")
				//Confirmed
			 }, function(dismiss){
				if(dismiss == 'cancel'){
					//swal({}); //un-comment this line to add another sweet alert popup on cancel


				}
			});
		},
		addNewDeposito: function() {
			// create new depos
			console.log("Nuevo Deposito....")
			var _header = { headers: { "X-CSRFToken": csrftoken } };
				//var data = new FormData();
				var data = this.makeDepositoData(this.deposito);  //estos son los datos a almacenar
				var url = URLS.endpoints.deposAdd(); //agara un url donde se mandan los datos para almacenar
				console.log(this.deposito.banco)
				console.log(data)
				this.$http.post(url, data, _header).then(
					function(response) {

						this.deposito_invoice = response.body;
						console.log("DEPOSITO ALMACENADO", response)
						toastr.success("El Deposito se ha almacenado correctamente", "<h6>Almacenado correctamente</h6>");
						//window.location.href = URL_LIST;

					},
					function(responseError) {
						console.log("ERROR");
						console.log(responseError);
					}

				);

		},
		loadClienteDeposito: function() {
			console.log("Cargando Clientes==>");
			var url = URLS.endpoints.clienteDeposito();
			self = this;
			this.clientes = [];
			clientes = [];

				data = this.cliente;

			this.$http.get(url, { 'params': data }).then(
				function(response) {
					clientes = response.body;
					console.log(clientes)
					for (item in clientes) {
						console.log(item)
						clientes[item] = clientes[item]
					}
					//console.log(ciudades)
					this.clientes = clientes;
					ClienteDepositoTypeahead.init(this.clientes);
				},
				function(responseError) {
					//console.log("ERROR", responseError);
					this.clientes = [];

					//KTTypeahead.init(this.ciudades);
				}

			);

		},
		loadBanco: function(){
			console.log("****** Cargando lista de bancos ******")
			var url = URLS.endpoints.listbanco();
			this.$http.get(url).then(
				function(response) {
					this.bancos = response.body.results;
					console.log("******", this.bancos);

				},
				function(responseError) {
					console.log("ERROR");
					console.log(responseError);
				}
			);
		},
		makeDepositoData: function(data_input) {
			var data = new FormData();

			if (!!data_input.codigo_asesor){
				data.append("codigo_asesor", data_input.codigo_asesor);
			}

			if (!!data_input.prestamo){

				data.append("prestamo", data_input.prestamo);
			}
			if (!!data_input.codigo_cliente){
				data.append("codigo_cliente", data_input.codigo_cliente);
			}
			if (!!data_input.fecha) {
				data.append("fecha", data_input.fecha);
			}

			if (!!data_input.banco){console.log(data.banco)
				data.append("banco", data_input.banco);
			}
			if (!!data_input.importe){
				data.append("importe", data_input.importe);
			}
			if (!!data_input.observaciones){
				data.append("observaciones", data_input.observaciones);
			}

			if (!!this.$refs.avatarFile.files.length > 0){
				console.log("imageeee:",  this.$refs.avatarFile.files);
				data.append('image', this.$refs.avatarFile.files[0]);
			}else{
				console.log("notiene imagen");
			}


			console.log("datta",data);
			return data;
		},
		getDeposito: function(pk) {
			var url = URLS.endpoints.getDeposito(pk);
			console.log(url);
			//this.cliente_edit = null;
			this.deposito_edit = DEPOSITO_EDIT;

			this.$http.get(url).then(function(response) {
				this.deposito_edit = response.body
				this.deposito_edit.banco = this.deposito_edit.banco.id;
				//this.getDatosAdicionalesCliente(this.cliente_edit.datos_adicionales.domiciliothis.cliente_edit.lugar_nacimiento)
				console.log("Retornando deposito: ", this.deposito_edit);
				this.image_url = "url("+this.deposito_edit.image+")";
				this.modal.editarDeposito.modal('show');

			}, function(responseError) {
				console.log(responseError)
			});
		},
		deleteDeposito:function(pk){
			var url = URLS.endpoints.deleteDeposito(pk);
			console.log("Eliminando deposito", pk, url);

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
			}).then(function(result) {
				if (result.value) {
					console.log("eliminando nuevo deposito...")
					self.$http.put(url, {}, _header).then(
						function(response){
							console.log("eliminado")
						},
						function(responseError){
							console.log("ERROR eliminado")
						}
					);
					window.location.href = URL_LIST;
				}
			});
		},
		editDeposito:function(pk){
			var url = URLS.endpoints.deleteDeposito(pk);
			console.log("Eliminando deposito", pk, url);
			var self = this;
			Swal.fire({
				title: "¿Está seguro?",
				text: "Se actualizaran los datos del deposito.",
				icon: "warning",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, actualizar!",
				cancelButtonText: "No, cancelar",
				customClass: {
					confirmButton: "btn font-weight-bold btn-success",
					cancelButton: "btn font-weight-bold btn-default"
				}
			}).then(function(result) {
				self.saveEditDeposito(pk)
			});
		},
	},
	mounted: function() {
		console.log("Cargando Lista de depositos");
		DatepickerDeposito.init();
		//this.setListaDepositos();
		//this.loadListDepositos();
		//this.loadListClientes();
		//this.loadClienteDeposito();
		ClienteDepositoTypeahead.init();
		//this.addNewDeposito();
		//this.previewaddNewDeposito();
		this.loadBanco();
		this.modal.editarDeposito = $(this.$refs.editModalDeposito);


	},

})