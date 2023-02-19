CUENTAS = [
  "ACTIVOS INTAGIBLES",
  "EQUIPOS DE COMPUTACION",
  "EQUIPOS DE COMUNICACIONES",
  "EQUIPOS DE SEGURIDAD",
  "EQUIPOS DE EDUCACION Y RECREATIVO",
  "HERRAMIENTAS EN GENERAL",
  "MAQUINARIA EN GENERAL",
  "MATERIAL DE ESCRITORIO",
  "MUEBLES Y ENSERES DE OFICINA",
  "VEHICULOS",
  "OTROS ACTIVOS FIJOS",
];
let ACTIVO = {
  codigo: null,
  cuenta: null,
  activo: null,
  descripcion: null,
  estado: null,
  responsable: null,
  ubicacion: null,
  departamento: null,
  agencia: null,
  obsercaciones: null,
  imagen: null,
  fecha_adquisicion: null,
  precio_compra: null,
  valor_revaluo: null,
  fondos: null,
};
let ACTIVO_DATA = {
  codigo: null,
  cuenta: "EQUIPOS DE COMPUTACION",
  activo: "Teclado mecanico",
  descripcion: "Teclado para desarrolladores de software",
  estado: "BU",
  responsable: "Eliot Alderson",
  ubicacion: "2do. piso",
  departamento: "SISTEMAS",
  agencia: "EL CARMEN",
  obsercaciones: null,
  imagen: null,
  fecha_adquisicion: null,
  precio_compra: 150,
  valor_revaluo: 100,
  fondos: "A",
};
var app = new Vue({
  el: "#kt_content_activos",
  data: {
    error: {
      codigo: null,
      cuenta: null,
      activo: null,
      descripcion: null,
      estado: null,
      codigo: null,
      responsable: null,
      ubicacion: null,
      departamento: null,
      agencia: null,
      obsercaciones: null,
      imagen: null,
      fecha_adquisicion: null,
      precio_compra: null,
      valor_revaluo: null,
    },
    activo_fijo: ACTIVO,
    error_activo: ACTIVO,
    new_activo: null,
    modal: {
      editActivo:null,
      importActivo:null,
      addFoto:null,
    },
    image_url: null,
    url_foto: null,
    fotos: [],
    fotos_activo: [],
    foto_default: null,
    filtrar_activo: {
      codigo: null,
      cuenta: null,
      estado: null,
      responsable: null,
      departamento: null,
      agencia: null,
      activo: null,
      fecha_adquisicion_ini: null,
      fecha_adquisicion_fin: null,
      precio_compra: null,
      valor_revaluo: null,
    },
    list_filter: [],
    list_activos: [],
    formularioReporte: null,
    id_activo: null,
  },
  computed: {
    codigo_message: function () {
      let message = this.error_activo.codigo[0].message;
      return message;
    },
    codigo_error: function () {
      if (this.error_activo.codigo) {
        return true;
      }
    },
    buildImageUrl: function () {
        return 'background-image: url("' + this.activo_fijo.imagen + '") '
    }
  },

  methods: {
    openModalImportActivo: function () {
      this.modal.importActivo.modal('show');
    },
    closeModalImportActivo: function(){
      this.modal.addFoto.modal('hide'); 
    },
    closeModalAddFoto: function () {
      //console.log("cerrando modal agregar foto")
      //window.location.href = URL_LIST;
      this.modal.addFoto.modal('hide'); 
    },
    openModalAddFoto: function (id) {
      this.id_activo = id;
      this.url_foto = URLS.endpoints.fotoActivoAddList(id);
      this.getFotosForActivo(id);
      //console.log("open modal Add Foto: ", this.url_foto);  
      this.modal.addFoto.modal('show');
    },
    openModalEditActivo: function(id){
      //console.log("open modal Edit: ", id);
      this.getActivo(id)
      this.modal.editActivo.modal('show');
    },
    closeModalEditActivo: function(){
      //console.log("close modal Edit: ");
      this.modal.editActivo.modal('hide'); 
    },
    getFotosForActivo: function(id) {
      /**
       *This function return fotos for activo fijo selected 
       */
      var url_imagen = URLS.endpoints.getImagenActivoFijo(id);
      var url = URLS.endpoints.fotoActivoAddList(id);
      
      this.$http.get(url_imagen).then(function(response) {
        this.foto_default = response.body;
        //Cargando la imagen del activo pasivo en el modal
        //console.log("Retornando fotos por defecto del activo: ", this.foto_default);
      }, function(responseError) {
          console.log(responseError)
      });
      
      this.$http.get(url).then(function(response) {
        this.fotos_activo = response.body;
        //Cargando la imagen del activo pasivo en el modal
        //console.log("Retornando fotos del activo: ", this.fotos_activo);
      }, function(responseError) {
          console.log(responseError)
      });
    },
    getActivo: function(id) {
      /**
       *This function return activo fijo selected 
       */

      //console.log("Cargando Activo Fijo");
      var url = URLS.endpoints.getActivoFijo(id);
      
      this.$http.get(url).then(function(response) {
        this.activo_fijo = response.body
        // Cargando la imagen del activo pasivo en el modal

        //this.image_url = "url("+this.activo_fijo.imagen+")";
        this.foto = "url("+this.activo_fijo.imagen+")";
        //console.log("Retornando fotos de activo: ", this.activo_fijo);

      }, function(responseError) {
          console.log(responseError)
      });
    },
    deleteActivo: function(id) {
      /**
       *This function delete activo fijo selected 
       */

      var url = URLS.endpoints.getActivoFijo(id);
      var _header = { headers: { "X-CSRFToken": csrftoken } };
      self=this;

      Swal.fire({
        title: "¿Está seguro?",
        text: "Se eliminará el activo fijo.",
        icon: "error",
        showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "Si, eliminar",
        cancelButtonText: "No, cancelar",
        customClass: {
            confirmButton: "btn font-weight-bold btn-danger",
            cancelButton: "btn font-weight-bold btn-default"
        }
      }).then(function(result) {
          if (result.value) {
            //console.log("eliminando item")
            self.$http.delete(url, _header).then(function(response) {
              self.activo_fijo = response.body
              // Cargando la imagen del activo fijo en el modal
              toastr.error("<h6>Eliminado</h6>");
              window.location.href = URL_LIST;
      
            }, function(responseError) {
                console.log(responseError)
            });
          } 
      }); 
      
    },
    editActivo: function() {
      /**
       * edit activo fijo 
       */
      //console.log("Actualizando activo");

      if (!!this.$refs.imagenFile && this.$refs.imagenFile.files.length > 0) {
        this.activo_fijo.imagen = this.$refs.imagenFile.files[0];
        //console.log("cargando imagen", this.activo_fijo.imagen);
      }

      var url = URLS.endpoints.putActivoFijo(this.activo_fijo.id);
      var _header = { headers: { "X-CSRFToken": csrftoken } };
      var data = this.makeActivoFijoData();

      var self = this;
      
      Swal.fire({
          title: "¿Está seguro?",
          text: "Se actualizarna los datos del activo fijo.",
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
              //console.log("actualizando activo...")
              self.$http.put(url, data, _header).then(function(response) {
                self.activo_fijo = response.body
                toastr.success("Se ha actualizado correctamente el activo fijo", "<h6>Actualizacion correcto</h6>");
                self.closeModalEditActivo();
                //window.location.href = URL_LIST;
              }, function(responseError) {
                  console.log(responseError)
              });
          } 
      });   
    },
    // Metodo para crear un nuevo activo fijo
    createActivo: function () {
      console.log("Creando activo");
      /*
      if (!!this.$refs.imagenFile && this.$refs.imagenFile.files.length > 0) {
        this.activo_fijo.imagen = this.$refs.imagenFile.files[0];
        console.log("cargando imagen", this.activo_fijo.imagen);
      }
      */
      
      var url = URLS.endpoints.postActivoFijo(this.activo_fijo.id);
      var _header = { headers: { "X-CSRFToken": csrftoken } };
      //var data = this.makeActivoFijoData();
      var data = this.activo_fijo
      var self = this;
      console.log(data)
      Swal.fire({
          title: "¿Está seguro?",
          text: "Se almacenaran los datos del nuevo activo fijo.",
          icon: "warning",
          showCancelButton: true,
          buttonsStyling: false,
          confirmButtonText: "Si, crear",
          cancelButtonText: "No, cancelar",
          customClass: {
              confirmButton: "btn font-weight-bold btn-success",
              cancelButton: "btn font-weight-bold btn-default"
          }
      }).then(function(result) {
        if (result.value) {
          console.log("creando activo...")
          self.$http.post(url, data, _header).then(function(response) {
            self.new_activo = response.body;
            
            self.url_foto = URLS.endpoints.fotoActivoAddList(self.new_activo.id);
            toastr.success("Se ha creado correctamente el activo fijo", "<h6>Actualizacion correcto</h6>");
            if (!!self.$refs.imagenFile && self.$refs.imagenFile.files.length > 0) {
              self.postFotoActivo(self.new_activo.id);
            } else {
              window.location.href = URL_LIST;
            }
          }, function(responseError) {
            self.error_activo = responseError.body;
            console.log(self.error_activo);
          });
        } 
      }); 
    },
    importActivos: function(){
      console.log("Importando excel")
    },    
    makeActivoFijoData: function() {
      /**
       * generate an data set elemento for send to edit method
       */
      var data = new FormData();
      if (!!this.activo_fijo.codigo)
          data.append("codigo", this.activo_fijo.codigo);

      if (!!this.activo_fijo.cuenta)
          data.append("cuenta", this.activo_fijo.cuenta);

      if (!!this.activo_fijo.activo)
          data.append("activo", this.activo_fijo.activo);

      if (!!this.activo_fijo.estado)
          data.append("estado", this.activo_fijo.estado);

      if (!!this.activo_fijo.descripcion)
          data.append("descripcion", this.activo_fijo.descripcion);

      if (!!this.activo_fijo.responsable)
          data.append("responsable", this.activo_fijo.responsable);

      if (!!this.activo_fijo.ubicacion)
          data.append("ubicacion", this.activo_fijo.ubicacion);

      if (!!this.activo_fijo.departamento)
          data.append("departamento", this.activo_fijo.departamento);

      if (!!this.activo_fijo.agencia)
          data.append("agencia", this.activo_fijo.agencia);

      if (!!this.activo_fijo.observaciones)
          data.append("observaciones", this.activo_fijo.observaciones);

      if (!!this.activo_fijo.fecha_adquisicion)
          data.append("fecha_adquisicion", this.activo_fijo.fecha_adquisicion);

      if (!!this.activo_fijo.precio_compra)
          data.append("precio_compra", this.activo_fijo.precio_compra);

      if (!!this.activo_fijo.valor_revaluo)
          data.append("valor_revaluo", this.activo_fijo.valor_revaluo);

      if (!!this.activo_fijo.fondos)
          data.append("fondos", this.activo_fijo.fondos);

      if (!!this.$refs.imagenFile && this.$refs.imagenFile.files.length > 0){
          console.log("cargando imagen");
          data.append('imagen', this.$refs.imagenFile.files[0]);
      }
      return data;
    },
    makeActivoFilterData: function() {
      /**
       * generate an data set elemento for send to edit method
       */
      console.log("Seteando formulario filter");
      var data = new FormData();
      if (!!this.filtrar_activo.codigo)
          data.append("codigo", this.filtrar_activo.codigo.toUpperCase());

      if (!!this.filtrar_activo.cuenta)
          data.append("cuenta", this.filtrar_activo.cuenta.toUpperCase());

      if (!!this.filtrar_activo.activo)
          console.log("Cargando activo")
          data.append("activo", this.filtrar_activo.activo.toUpperCase());

      if (!!this.filtrar_activo.estado)
          data.append("estado", this.filtrar_activo.estado.toUpperCase());

      if (!!this.filtrar_activo.descripcion)
          data.append("descripcion", this.filtrar_activo.descripcion.toUpperCase());

      if (!!this.filtrar_activo.responsable)
          data.append("responsable", this.filtrar_activo.responsable.toUpperCase());

      if (!!this.filtrar_activo.ubicacion)
          data.append("ubicacion", this.filtrar_activo.ubicacion.toUpperCase());

      if (!!this.filtrar_activo.departamento)
          data.append("departamento", this.filtrar_activo.departamento.toUpperCase());

      if (!!this.filtrar_activo.agencia)
          data.append("agencia", this.filtrar_activo.agencia.toUpperCase());

      if (!!this.filtrar_activo.observaciones)
          data.append("observaciones", this.filtrar_activo.observaciones.toUpperCase());

      if (!!this.filtrar_activo.fecha_start)
          data.append("fecha_start", this.filtrar_activo.fecha_start);

      if (!!this.filtrar_activo.fecha_end)
          data.append("fecha_end", this.filtrar_activo.fecha_end);

      if (!!this.filtrar_activo.precio_compra)
          data.append("precio_compra", this.filtrar_activo.precio_compra);

      if (!!this.filtrar_activo.valor_revaluo)
          data.append("valor_revaluo", this.filtrar_activo.valor_revaluo);

      return data;
    },

    makeFotoActivoData: function(foto) {
      var data = new FormData();      
      data.append('foto', foto);
      return data;
    },
    
    postFotoActivo: function (pk) {
      /**
       *Carga la Foto del activo fijo 
       */
      var _header = { headers: { "X-CSRFToken": csrftoken } };
      //var url = URLS.endpoints.fotoActivoAddList(pk);
      
      if (!!this.$refs.imagenFile && this.$refs.imagenFile.files.length > 0) {
        this.activo_fijo.imagen = this.$refs.imagenFile.files[0];
        var data = this.makeFotoActivoData(this.activo_fijo.imagen);
        
        this.$http.post(this.url_foto, data, _header).then(function (response) {
          this.fotos_activo = response.body;
          if (this.fotos_activo.length > 0) {
            this.getFotosForActivo(this.id_activo);
            toastr.success("Se ha agregado la foto correctamente al activo fijo", "<h6>Foto almacenada</h6>");
            if (this.$refs.clearFile){this.$refs.clearFile.click();}
            this.activo_fijo.imagen = null;
            if (this.$refs.imagenFile.length > 0){this.$refs.imagenFile.files = [];}
          }
          //this.closeModalEditActivo();
          window.location.href = URL_LIST;
        }, function (responseError) {
          console.log(responseError);
        });
      } else {
          toastr.error("Carga una foto primero.", "<h6>Error</h6>");
      }

    },
    
    deleteFotoActivo: function (id_foto) {
      var _header = { headers: { "X-CSRFToken": csrftoken } };

      var url = URLS.endpoints.fotoActivoGetDelete(this.id_activo, id_foto);
      self = this;
      //console.log("eliminando foto ", id_foto);
      Swal.fire({
        title: "¿Está seguro?",
        text: "Se eliminara la fotografía.",
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
          //console.log("eliminando nuevo certificado...")
          self.$http.delete(url, _header).then(function (response) {
            self.fotos_activo = response.body;
            toastr.warning("Se ha eliminado la foto correctamente del activo fijo", "<h6>Foto eliminada</h6>");
            //self.closeModalEditActivo();
            //window.location.href = URL_LIST;
          }, function (responseError) {
            console.log(responseError);
          });
        }
      });
    },
    
    updateFotoActivoDefault: function (id_foto) {
      var _header = { headers: { "X-CSRFToken": csrftoken } };

      var url = URLS.endpoints.fotoActivoGetDelete(this.id_activo, id_foto);
      var data = {}
      self = this;
      //console.log("eliminando foto ", id_foto);
      Swal.fire({
        title: "¿Está seguro?",
        text: "Se cambiará la fotografía por defecto.",
        icon: "warning",
        showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "Si, cambiar!",
        cancelButtonText: "No, cancelar",
        customClass: {
          confirmButton: "btn font-weight-bold btn-primary",
          cancelButton: "btn font-weight-bold btn-default"
        }
      }).then(function(result) {
        if (result.value) {
          //console.log("eliminando nuevo certificado...")
          self.$http.put(url, data, _header).then(function (response) {
            self.foto_default = response.body;
            //self.loadListActivos();
            toastr.info("Se ha actualizafo la foto por defecto correctamente", "<h6>Foto por defecto</h6>");
            //self.closeModalEditActivo();
            window.location.href = URL_LIST;
          }, function (responseError) {
            console.log(responseError);
          });
        }
      });
    },

    loadListActivos: function () {
      var url = URLS.endpoints.getListActivoFijo();

      this.$http.get(url).then(function(response) {
        this.list_filter = response.body;
        this.list_activos = this.list_filter;

        
        //window.location.href = URL_LIST;
      }, function(responseError) {
        toastr.success("Error al cargar lista de activos fijos", "<h6>error!</h6>");
        console.log(responseError)
      });  
    },

    nextPreviousPage: function (url) {
      this.$http.get(url).then(function(response) {
        this.list_filter = response.body
        this.list_activos = this.list_filter
      }, function(responseError) {
        toastr.success("Error al cargar lista de activos fijos", "<h6>error!</h6>");
        console.log(responseError)
      });  
    },
    
    downloadExcel: function () {
      var formulario = this.$refs.formReporte;
      formulario.action = URL_REPORT;
      formulario.submit();
    },
    filterActivos: function () {
      var formulario = this.$refs.formReporte;
      formulario.action = URL_FILTER;
      formulario.submit();
    },
    generateCodigo: function () {
      /** TODO: automatizar esta funcion sin necesidad de ejecutarlo con el boton */
      var agencia = this.getCodigoAgencia(this.activo_fijo.agencia);
      var cuenta = this.getCodigoCuenta(this.activo_fijo.cuenta);
      var departamento = this.getCodigoDepartamento(this.activo_fijo.departamento);
      this.activo_fijo.codigo = "JGP-" + agencia + "-" + cuenta + "-" + departamento + "-";

      /* Load toastr options */ 
      toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": true,
        "progressBar": true,
        "positionClass": "toastr-top-center",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
      };
      toastr.info("Completalo por favor.", "Código generado");
    },
    getCodigoCuenta(cuenta) {
      if(cuenta=="MUEBLES Y ENSERES DE OFICINA"){return "01"; }
      else if(cuenta=="MAQUINARIA EN GENERAL"){return "02"; }
      else if(cuenta=="EQUIPOS DE COMPUTACION"){return "03"; }
      else if(cuenta=="EQUIPOS DE COMUNICACIONES"){return "04"; }
      else if(cuenta=="EQUIPOS DE SEGURIDAD"){return "05"; }
      else if(cuenta=="EQUIPOS DE EDUCACION Y RECREATIVO"){return "06"; }
      else if(cuenta=="HERRAMIENTAS EN GENERAL"){return "07"; }
      else if(cuenta=="OTROS ACTIVOS FIJOS"){return "08"; }
      else if(cuenta=="ACTIVOS INTAGIBLES"){return "09"; }
      else if(cuenta=="VEHICULOS"){return "10"; }
      else if (cuenta == "MATERIAL DE ESCRITORIO") { return "11"; }
      else { return null; }
    },
    getCodigoAgencia(agencia) {
      if(agencia=="REGIONAL") {return "99"; }
      else if(agencia=="EL CARMEN") {return "00"; }
      else if(agencia=="BUENOS AIRES") {return "01"; }
      else if(agencia=="MINISUR") {return "04"; }
      else if(agencia=="PAMPAHASI") {return "05"; }
      else { return null; }
    },
    getCodigoDepartamento(departamento) {
      if(departamento == "ADMINISTRACION") { return "ADM";}
      else if(departamento == "ASESORIA COMERCIAL") { return "ASC";}
      else if(departamento == "ASESORIA LEGAL") { return "ASL";}
      else if(departamento == "ATENCION AL CLIENTE") { return "ATC";}
      else if(departamento == "BAÑO") { return "BAÑ";}
      else if(departamento == "CAJA") { return "CAJ";}
      else if(departamento == "COCINA") { return "COC";}
      else if(departamento == "CONTABILIDAD") { return "CON";}
      else if(departamento == "DEPOSITO") { return "DEP";}
      else if(departamento == "ENTRADA") { return "ENT";}
      else if(departamento == "FRONTIS") { return "FRO";}
      else if(departamento == "GERENCIA DE AGENCIA") { return "GDA";}
      else if(departamento == "GERENCIA GENERAL") { return "GGO";}
      else if(departamento == "GERENCIA OPERATIVA Y COMERCIAL") { return "GOC";}
      else if(departamento == "GRADAS") { return "GRA";}
      else if(departamento == "NORMALIZACION") { return "NOR";}
      else if(departamento == "PASILLO") { return "PAS";}
      else if(departamento == "PLATAFORMA") { return "PLA";}
      else if(departamento == "GESTION DE TALENTO HUMANO") { return "GTH";}
      else if(departamento == "SECRETARIA") { return "SEC";}
      else if(departamento == "SISTEMAS") { return "SIS";}
      else { return null; }
    },
  },
  mounted: function() {
    
    this.modal.editActivo = $(this.$refs.editModalActivo);
    this.modal.addFoto = $(this.$refs.addModalFotos);
    this.modal.importActivo = $(this.$refs.importModalActivo);
    console.log(this.image_url)
    /*
    DatepickerAdquisicion.init();
    DatepickerAdquisicionIni.init();
    DatepickerAdquisicionFin.init();
    */
    //this.modal.editActivo.modal('show');
    //this.modal.addFoto.modal('show');

  }
})