var csrf_token = { headers: { "X-CSRFToken": csrftoken } };

var RECLAMO = {
    nombre_completo: null,
    numero_celular: null,
    detalle: null,
};

var csrf_token = { headers: { "X-CSRFToken": csrftoken } };

var DATA_RECLAMO = {
    nombre_completo: null,
    cedula_identidad: null,
    numero_celular: null,
    detalle: null,
};

var app = new Vue({
	el: '#id_landing',
	data: {
		ubicacion: null,
		lista_sucursales: null,
		lista_sucursales: null,
		modal: {
			ubicacionSucursal: null,
			reclamos: null,
		},
    nombre_completo_sucursal: null,
		reclamo_completo: DATA_RECLAMO,
    /**
     
     nombre_completo: null,
     numero_celular: null,
     detalle: false,
     nombre_completo: null,
     */
		reclamo: DATA_RECLAMO,
		error_reclamo: DATA_RECLAMO,
	},
	methods: {
		loadPunto: function (punto_gps) {
			punto_array = punto_gps.split(',');
			punto =  { lat: parseFloat(punto_array[0]), lng: parseFloat(punto_array[1])};
			return punto
		},
		openUbicacionModal: function(punto_gps, nombre ) {
			this.nombre_completo_sucursal = nombre;
			if (!!this.$refs.map) { initMap(this.loadPunto(punto_gps)); }
			this.modal.ubicacionSucursal.modal('show');
		},
		closeModalUbicacion: function () {
			this.ubicacion = null;
			this.modal.ubicacionSucursal.modal('hide');
		},

		sendReclamo: function (){
			var self=this;
			
			Swal.fire({
				title: "¿Está seguro?",
				icon: "warning",
				showCancelButton: true,
				buttonsStyling: false,
				confirmButtonText: "Si, enviar reclamo!",
				cancelButtonText: "No, cancelar",
				customClass: {
				confirmButton: "btn font-weight-bold btn-success",
				cancelButton: "btn font-weight-bold btn-default"
				}
				
			}).then(function (result) {
				if (result.value) {
				  var url = URLS.endpoints.postReclamos();
		
				  self.$http.post(url, self.reclamo, csrf_token).then(
						function (response) {						
							toastr.success("El reclamo se ha almacenado correctamente", response.data);
							this.modal.reclamos.modal('hide');
					  },
            function (responseError) {
              self.error_reclamo = responseError.data;
              toastr.error("Error al almacenar el reclamo", responseError.data);
            }              
          );
				}
			});
		},
		closeModalReclamo: function (){
      this.reclamo = DATA_RECLAMO;
      this.modal.reclamos.modal('hide');
    },
		getListSucursales: function (){
			url = URLS.endpoints.getSucursales();

			this.$http.get(url).then(
				function(response){
					this.lista_sucursales = response.body;
				},        
				function(responseError) {
					console.log(responseError);
				}
			);
		},

	},
	mounted: function () {
		this.modal.reclamos = $(this.$refs.reclamoModal);
		this.modal.ubicacionSucursal = $(this.$refs.sucursalModal);
		this.getListSucursales();
	},
});
