let CSFR_TOKEN = { headers: { "X-CSRFToken": csrftoken } };
let app = new Vue(
  {
    el: '#kt_wrapper',
    data: {
      enlace_formulario: null,
      solicitudes: null,
      table: null,
      form_solicitud: null,
      desembolsado: null,
      solicitud: null,
      complemento: null,
      documentos: null,
      asesor_asignado: null,
      form_solicitud: {
        destino: null,
        estado_solicitud: null,
        comentario_revision: null,
        monto_sugerido: null,
      },
      users: null,
      usuario_asesor: null,
      modals: {
        asesores:null,
        enlace:null,
        usuario_estadistica:null,
        filter_list_solicitud:null,
      },
      opcion: {
        fecha_inicial: null, // "2022-02-08",
        fecha_final: null, // "2022-02-10",
      },
      solicitud_filter: null,
      error: {
        filter: null,
      },
    },
    computed: {
      url_foto: function () {
        /** Return foto url of solicitud selected */
        if(this.solicitud && this.solicitud.foto){
          return this.solicitud.foto;
        } else{
          return FOTO_DEFAULT;
        }
      },
      estado_solicitud: function(){
        /** return complete name tipo solicitud */
        if(this.solicitud.estado_solicitud == 'SO'){
          return 'Solicitado';
        } else if(this.solicitud.estado_solicitud == 'FI'){  
          return 'Finalizado';
        } else if(this.solicitud.estado_solicitud == 'SC'){  
          return 'Solicitud Complemento';
        } else if(this.solicitud.estado_solicitud == 'EL'){  
          return 'Eliminado';
        } else if(this.solicitud.estado_solicitud == 'AS'){  
          return 'Asignado';
        } else if(this.solicitud.estado_solicitud == 'RE'){  
          return 'Revisado';
        } else if(this.solicitud.estado_solicitud == 'CO'){  
          return 'Contactado';
        } else if(this.solicitud.estado_solicitud == 'AP'){  
          return 'Aprobado';
        } 
      }
    },
    watch: {
    },
    methods: {
      listSolicitudes: function () {
        /** Return solicitudes list */
        var url = URLS.endpoints.ListCreateCredito();
        
        this.$http.get(url).then(
          function(response){
            this.solicitudes = response.body;
          },
        );
      },
      getSolicitud: function(slug) {
        /** Load solicitud from slug */
        var url = URLS.endpoints.getSolicitud(slug);
        
        this.$http.get(url).then(function(response) {
          this.solicitud = response.body.solicitud;
          this.complemento = response.body.complemento;
          this.documentos = response.body.documentos;
          this.asesor_asignado = response.body.asesor_asignado;
  
          this.form_solicitud = this.solicitud;
          /*
          this.form_solicitud.destino = this.solicitud.destino;
          this.form_solicitud.estado_solicitud = this.solicitud.estado_solicitud;
          this.form_solicitud.comentario_revision = this.solicitud.comentario_revision;
          this.form_solicitud.monto_sugerido = this.solicitud.monto_sugerido;
          this.form_solicitud.desembolsado = this.solicitud.desembolsado;
          this.form_solicitud.fecha_desembolso = this.solicitud.fecha_desembolso;
          */
        }, function(responseError) {
          console.log(responseError)
        });
      },
      updateSolicitud: function (slug) {
        /** Function for update a solicitud */
        var url = URLS.endpoints.updateSolicitud(slug);
        var data = this.form_solicitud;
        data.usuario= USER;
        
        this.$http.put(url, data, CSFR_TOKEN).then(
          function(response){
            this.solicitud = response.body;
            toastr.success("Datos actualizados", "Almacenado correctamente");
          },
          function(errorResponse){
            toastr.error("Datos actualizados", "Error al almacenar");
            this.success = false;
            console.log(errorResponse);
          },
        );
      },
      deleteSolicitud: function (slug) {
        /** Function for delete a solicitud */
        var url = URLS.endpoints.deleteSolicitud(slug);
        var _header = CSFR_TOKEN;
        var data = {'estado_solicitud':'EL'};
        
        this.$http.put(url, data, _header).then(
          function(response){
            this.solicitud_success = response.body;
            window.location.href = URL_LIST;
          },
          function(errorResponse){
            this.success = false;
          },
        );
      },

      generarFormComplemento: function (slug) {
        /**Create url for 2nd. form solicitud */
        var url = URLS.endpoints.urlFormularioComplemento(slug);
        this.enlace_formulario =  url;
      },
      sendWathsappFormulario: function () {
        /** Generate message and url 2nd. form for whatsapp send */
        this.generarFormComplemento(this.solicitud.slug);
        var url_whatsapp = "https://wa.me/%2B591"+this.solicitud.whatsapp+"?"
          + "text=Estimad@%20" + this.solicitud.nombres
          + "%20*¡Tu%20solicitud%20ha%20sido%20revisado!*,"
          + "%0APor%20favor%20ahora%20puedes%20llenar%20el%20siguiente%20formulario:%0A"
          + this.enlace_formulario;
        window.open(url_whatsapp, "_blank");
      },
      sendWhatsapp: function (number) {
        /**Send message on whatsapp */
        if( !!number){
          whatsapp_number = number;
        } else{
          whatsapp_number = this.solicitud.whatsapp;
        }

        var url_whatsapp = "https://wa.me/%2B591" + whatsapp_number;          
        window.open(url_whatsapp, "_blank");
      },
      toggleModalAsesor: function(){
        /** Function for open modal and load asesores in self */
        this.modals.asesores.modal('show');
        this.loadUsers();
      },
      toggleModalUsuarioEstadistica: function(asesor){
        /** Function for open modal and load asesores in self */
        this.getAssesor(asesor);
        this.modals.usuario_estadistica.modal('show');
      },
      loadUsers:function(){
        /**Load list asesores users for assing to solicitud */
        let url = URLS.endpoints.getUsers();
        if (!this.users) {
          this.$http.get(url).then(function(response){
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
      getAssesor:function(asesor){
        /**Load list asesores users for assing to solicitud */
        let url = URLS.endpoints.getAssesor(asesor);
        this.$http.get(url).then(function(response){
          if (!!response.body) {
            this.usuario_asesor = response.body;
          }else{
            toastr.error("Error al cargar asesor", "Error al cargar asesor");
          }
        }, function(errorResponse){
          console.log("error al cargar usuarios", errorResponse);
          toastr.error("Error al cargar asesor", "Error al cargar asesor");
        });
      },
      toggleAssignAdviser:function (asesor){
        /**Function for assign and unassign asesor to solicitud */
        let data = {
          'asesor': asesor,
          'usuario': USER,
        }
        let url = URLS.endpoints.assignAdviser(SLUG);
        //console.log("asignando usuario", data, url);

        this.$http.put(url, data, CSFR_TOKEN).then(
          function(response){
            this.solicitud = response.body;
            this.modals.asesores.modal('hide');
            if(asesor=="null"){
              toastr.warning("Asesor desasignado", "Asesor desasignado");
            }else{
              toastr.success("Asesor asignado correctamente", "Asesor asignado");
            }
          }, function(errorResponse){
            console.log("Error al asignar usuario", errorResponse);
          }
        );
      },
      openLinkFormModal: function (slug) {
        /** Generate url 2nd. form for modal */
        this.generarFormComplemento(slug);
        this.modals.enlace.modal('show');
      },      
      copyText: function (text) {
        /** Function for copy text on clipboard */
        toastr.info("", "Url copiado");
        return navigator.clipboard.writeText(text);
      },
      filterSolicitudes: function(){
        //console.log("filtrando solicitudes", this.opcion.fecha_inicial, " - ", this.opcion.fecha_final, "\n", CSFR_TOKEN);
        let url = URLS.endpoints.filtersolicitudRangeDate();
        let data = this.opcion;
        var _header = CSFR_TOKEN;

        this.$http.put(url, data, _header).then(
          function(response){
            this.solicitud_filter = response.body;
            console.log("RESULTADO: ", this.solicitud_filter)
            //toastr.success("Solicitudes filtradas", "Solicitudes filtradas");
            this.modals.filter_list_solicitud.modal('show');
            
          }, function(errorResponse){
            console.log("error al cargar filtrado de solicitudes", errorResponse);
            this.error.filter = errorResponse.body;
            //toastr.error("Error al cargar filtrado de solicitudes", "Error al cargar filtrado de solicitudes");444
          }
        );
      },
      clearFilter: function(){
        this.opcion = {
          fecha_inicial: null,
          fecha_final: null,
        }
        this.modals.filter_list_solicitud.modal('hide');
      },
    },
    mounted: function() {
      this.modals.asesores = $(this.$refs.modalAsesores);
      this.modals.usuario_estadistica = $(this.$refs.modalUsuariosEstadistica);
      this.modals.enlace = $(this.$refs.modalEnlaceFormulario);
      this.modals.filter_list_solicitud = $(this.$refs.modalFilterListSolicitud);
    }
  }
)