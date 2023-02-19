/** Vue for cliente model for API-Cliente conect and functions extra
 * TODO: Implmentar select de PROVINCIAS y demas de ubicacion
 */
var app = new Vue({
  el: "#kt_content",
  data: {
    show_secundaria: true,
    show_referencia: true,
    fecha: {
      dia: null,
      mes: null,
      año: null,
    },
    cliente: JSON.parse(JSON.stringify(CLIENTE)),
    domicilio: JSON.parse(JSON.stringify(DOMICILIO)),
    conyuge: JSON.parse(JSON.stringify(CONYUGE)),
    conyuge_trabajo: JSON.parse(JSON.stringify(UBICACION_TRABAJO_CONYUGE)),
    actividad: JSON.parse(JSON.stringify(ACTIVIDAD)),
    direccion_actividad: JSON.parse(JSON.stringify(DIRECCION_ACTIVIDAD)),
    actividad_2: JSON.parse(JSON.stringify(ACTIVIDAD)),
    direccion_actividad_2: JSON.parse(JSON.stringify(DIRECCION_ACTIVIDAD)),
    referencia: JSON.parse(JSON.stringify(REFERENCIA)),
    referencia_2: JSON.parse(JSON.stringify(REFERENCIA)),
    validate: {
      telefono_1: null,
      telefono_2: null,
      telefono_referencia: null,
      telefono_referencia_2: null,
      telefono_conyuge: null,
      telefono_actividad: null,
      telefono_actividad_2: null,
    },
    atras: null,
    clientes: null,
    //cliente: null,
    level: false,
    clienteError: null,
    lista_ciudades_domicilio: [],
    lista_ciudades_conyuge: [],

    // desde aqui no se esta usando las variables
    actividad_economica: {
      cliente: null,
      actividad: null,
      es_principal: false,
      anios: "3",
      tipo: null,
      dias: "lunes, martes, miercoles, jueves, viernes, sabado, domingo",
      hora_inicio: "08:00",
      hora_fin: "18:00",
      tipo_ingresos: null,
      ciclo_rotacion: null,
      estado_rotacion: null,
      ingreso_mensual: null,
      ubicacion: {
        departamento: null,
        provincia: null,
        ciudad_comunidad: null,
        zona_urbanizacion: "Nicanor Melek",
        calle_avenida: "123123",
        nombre_vivienda: null,
        numero_vivienda: "45",
        ubicacion_gps: null,
        años_residencia: 0,
        tipo_tenencia: null,
        telefono: null,
      },
      estado: null,
    },
    referencia_personal: {
      cliente: null,
      nombre_apellido: "Gustavo Lopez",
      tipo_relacion: null,
      telefono: "2234567",
      radicatoria: {
        departamento: null,
        provincia: null,
        ciudad_comunidad: null,
      },
      calle_avenida: "Madrid",
      referencia_direccion: "Cerca del Santiago Bernabeu",
      estado: null,
    },
    errorCliente: {
      primer_nombre: [],
      apellido_paterno: [],
      numero_documento_identidad: [],
      fecha_nacimiento: [],
      extension_documento_identidad: null,
      años_residencia: [],
      tipo_tenencia: [],
      ubicacion_gps: [],
    },
    departamentos: DEPARTAMENTOS,
    provincias: [],
    provincias_domicilio: [],
    lista_provincias: PROVINCIAS,
    lista_ciudades: [],
    ciudades: [],
    marker: null,
    errorCliente: null,
    error: {
      primer_nombre: false,
      apellido_paterno: false,
      numero_documento_identidad: false,
      fecha_nacimiento: false,
      años_residencia: false,
      tipo_tenencia: false,
      ubicacion_gps: false,
    },
    //editModal: null,
    modal: {
      editarCliente: null,
      adicionarConyugue: null,
      adicionarReferenciaPersonal: null,
      adicionarActividadEconomica: null,
      adicionarClienteL1: null,
    },
    actividades: null,
    referencias: null,
    conyuges: null,
    next: null,
    previous: null,
    level1: false,
    level2: false,
    level3: false,
    list: true,
  },

  watch: {
    "domicilio.ubicacion.departamento": function(value) {
      this.filterCiudades(value, "domicilio");
      this.domicilio.ubicacion.ciudad_comunidad = null;
    },
    "conyuge_trabajo.ubicacion.departamento": function(value) {
      this.filterCiudades(value, "conyuge");
    },
    /**
     *
    'cliente.telefono_1': function (newValue, oldValue) {
          this.validate.telefono_1 = validateTelefono(newValue);
    },
    'cliente.telefono_2': function (newValue, oldValue) {
        this.validate.telefono_2 = validateTelefono(newValue);
    },
    'cliente.correo_electronico': function (newValue, oldValue) {
        this.validate.correo_electronico = validateEmail(newValue);
    },
    'referencia.telefono': function (newValue, oldValue) {
        this.validate.telefono_referencia = validateTelefono(newValue);
    },
    'referencia_2.telefono': function (newValue, oldValue) {
        this.validate.telefono_referencia_2 = validateTelefono(newValue);
    },
    'conyuge.telefono_1': function (newValue, oldValue) {
        this.validate.telefono_conyuge = validateTelefono(newValue);
    },
    'actividad.telefono': function (newValue, oldValue) {
        this.validate.telefono_actividad = validateTelefono(newValue);
    },
    'actividad_2.telefono': function (newValue, oldValue) {
        this.validate.telefono_actividad_2 = validateTelefono(newValue);
    },
    */
  },
  computed: {
    dias: function() {
      var array = [];
      for (i = 0; i < 31; i++) {
        array[i] = i + 1;
      }
      return array;
    },
    meses: function() {
      return MESES;
    },
    años: function() {
      var today = new Date();
      var year = today.getFullYear() - 90;
      var array = [];

      for (i = 0; i <= 72; i++) {
        array[i] = year;
        year++;
      }
      return array;
    },
    tiene_apellido_esposo: function() {
      if (
        this.cliente.genero == "F" &&
        (this.cliente.estado_civil_verificado == "C" ||
          this.cliente.estado_civil_verificado == "N")
      ) {
        return true;
      }
      return false;
    },
    tiene_conyuge: function() {
      if (
        this.cliente.estado_civil_verificado == "C" ||
        this.cliente.estado_civil_verificado == "N"
      ) {
        return true;
      }
      return false;
    },
    limite_domicilio_departamento: function() {
      return parseInt(this.domicilio.ubicacion.departamento) + 99;
    },
    limite_conyuge_departamento: function() {
      return parseInt(this.conyuge_trabajo.ubicacion.departamento) + 99;
    },
    limite_actividad_departamento: function() {
      return parseInt(this.direccion_actividad.ubicacion.departamento) + 99;
    },
    limite_actividad2_departamento: function() {
      return parseInt(this.direccion_actividad_2.ubicacion.departamento) + 99;
    },
    
  },
  methods: {
    toggleShowActividaSecundaria: function() {
      console.log("toggleShowActividaSecundaria");
      if (this.show_secundaria) {
        this.show_secundaria = false;
      } else {
        this.show_secundaria = true;
      }
    },
    toggleShowReferencia: function() {
      console.log("toggleShowReferencia");
      if (this.show_referencia) {
        this.show_referencia = false;
      } else {
        this.show_referencia = true;
      }
    },
    doMath: function(index) {
      return index + 1;
    },
    filterCiudades: function(departamento, key) {
      /** This function load ciudades in list */
      var url = URLS.endpoints.ubicacionProvinciaFilterCity();

      this.$http.put(url, { departamento: departamento }, csrf_token).then(
        function(response) {
          if (key == "domicilio") {
            //console.log("Cargando ciudades dpomicilio", response.body);
            this.lista_ciudades_domicilio = response.body;
            TypeaheadCiudad.init(response.body);
          }
          if (key == "conyuge") {
            //console.log("Cargando ciudades dpomicilio", response.body);
            this.lista_ciudades_conyuge = response.body;
          }
        },
        function(errorResponse) {
          console.log(
            "Error al cargar ciudades_comunidades",
            errorResponse.body
          );
        }
      );
    },

    /*
                    openLevel1: function(){
                        console.log("abriendo modal L1", this.modal.adicionarClienteL1);
                        this.modal.adicionarClienteL1.modal('show');
                        //this.modal.adicionarConyugue.modal('show');
                    },
                    openLevel2: function(){
                        this.level1 = false;
                        this.level2 = true;
                        this.level3 = false;
                        this.list = false;
                    },
                    openLevel3: function(){
                        this.level1 = false;
                        this.level2 = false;
                        this.level3 = true;
                        this.list = false;
                    },
                    openList: function(){
                        this.level1 = false;
                        this.level2 = false;
                        this.level3 = false;
                        this.list = true;
                    },
                    openEditModal: function(pk) {
                        console.log("abriendo modal para editar un cliente: ", pk);
                        this.getCliente(pk);
                    },
                    closeEditClienteModal: function(){
                        this.cliente_edit = CLIENTE_EDIT;
                        this.modal.editarCliente.modal('hide');
                        console.log("Clean Edit: ", this.cliente_edit )
                    },
                    openConyugueModal: function(cliente) {
                        this.conyuge.cliente = cliente;
                        this.conyuge.nombres = "Jose Maria";
                        this.conyuge.apellido_paterno = "Listorti";
                        this.conyuge.apellido_materno = "Prada";
                        this.conyuge.documento_identidad = "3238245 TA";
                        this.conyuge.fecha_nacimiento = null;
                        this.conyuge.lugar_nacimiento = {
                            "departamento": null,
                            "provincia": null,
                            "ciudad_comunidad": null,
                        };
                        this.conyuge.telefono = "2323233";
                        this.conyuge.direccion = null;
                        this.conyuge.ocupacion = "Locutor";

                        console.log("abriendo modal para adicionar Conyugue: ")
                        this.modal.adicionarConyugue.modal('show');
                    },
                    openReferenciaPersonalModal: function(cliente) {
                        this.referencia_personal.cliente= cliente;
                        this.referencia_personal.nombre_apellido= "Gustavo Lopez";
                        this.referencia_personal.tipo_relacion= null;
                        this.referencia_personal.telefono= "2234567";
                        this.referencia_personal.radicatoria= {
                            'departamento': null,
                            'provincia': null,
                            'ciudad_comunidad': null,
                        };
                        this.referencia_personal.calle_avenida= "Madrid";
                        this.referencia_personal.referencia_direccion= "Cerca del Santiago Bernabeu";
                        this.referencia_personal.estado= null;

                        console.log("abriendo modal para Referencia Personal: ")
                        this.modal.adicionarReferenciaPersonal.modal('show');
                    },
                    openActividadEconomicaModal: function(cliente) {
                        this.actividad_economica.cliente=cliente;
                        this.actividad_economica.actividad=null;
                        this.actividad_economica.es_principal=false;
                        this.actividad_economica.anios=3;
                        this.actividad_economica.tipo=null;
                        this.actividad_economica.dias="lunes, martes, miercoles, jueves, viernes, sabado, domingo";
                        this.actividad_economica.hora_inicio="08:00";
                        this.actividad_economica.hora_fin="18:00";
                        this.actividad_economica.tipo_ingresos=null;
                        this.actividad_economica.ciclo_rotacion=null;
                        this.actividad_economica.estado_rotacion=null;
                        this.actividad_economica.ingreso_mensual=null;
                        this.actividad_economica.ubicacion={
                            'departamento': null,
                            'provincia': null,
                            'ciudad_comunidad': null,
                            'zona_urbanizacion': "Nicanor Melek",
                            'calle_avenida': "123123",
                            'nombre_vivienda': null,
                            'numero_vivienda': "45",
                            'ubicacion_gps': null,
                            'años_residencia': 0,
                            'tipo_tenencia': null,
                            'telefono': null,
                        };
                        this.actividad_economica.estado=null;
                        if (!!this.$refs.map) { initMap(); }

                        console.log("abriendo modal para Actividad Economica: ")
                        this.modal.adicionarActividadEconomica.modal('handleUpdate');
                        this.modal.adicionarActividadEconomica.modal('show');
                    },
                    */
    loadListClientes: function() {
      // Caragando la lista de clientes
      var url = URLS.endpoints.clientes();
      this.$http.get(url).then(
        function(response) {
          this.next = response.body.next;
          this.previous = response.body.previous;
          this.clientes = response.body.results;
          //console.log(response.body)
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    
    getCliente: function(pk) {
      var url = URLS.endpoints.getCliente(pk);
      console.log(url);
      //this.cliente_edit = null;
      this.cliente_edit = CLIENTE_EDIT;

      this.$http.get(url).then(
        function(response) {
          this.cliente_edit = response.body;
          //this.getDatosAdicionalesCliente(this.cliente_edit.datos_adicionales.domiciliothis.cliente_edit.lugar_nacimiento)
          console.log("Retornando cliente: ", this.cliente_edit);
          /*
            if(!this.cliente_edit.lugar_nacimiento){
                this.cliente_edit.lugar_nacimiento = DEFAULT_LUGAR;
            } else{
                this.provincias = this.changeListProvincia(this.lista_provincias, this.cliente_edit.lugar_nacimiento.departamento);
            }

            if(!this.cliente_edit.datos_adicionales){
                this.cliente_edit.datos_adicionales = DATOS_ADICIONALES;
            }else{
                console.log("esxiste datos adicionales")
                if(!this.cliente_edit.datos_adicionales.domicilio){
                    console.log("sin domicilio")
                    this.cliente_edit.datos_adicionales.domicilio = DOMICILIO;
                }
                else{
                    console.log("hay domicilio")
                    this.provincias_domicilio = this.changeListProvincia(this.lista_provincias, this.cliente_edit.datos_adicionales.domicilio.ubicacion_base.departamento);

                }
                //this.provincias = this.changeListProvincia(this.lista_provincias, this.cliente_edit.datos_adicionales.domicilio.departamento);
            }
            if(!!this.cliente_edit.lugar_nacimiento) {
                //this.loadListProvincias('edit_lugar_nacimiento');
                this.provincias = this.changeListProvincia(this.lista_provincias, this.cliente_edit.lugar_nacimiento.departamento);

            }
            if(!!this.cliente_edit.datos_adicionales.domicilio) {
                //this.loadListProvincias("edit_domicilio");
                this.provincias_domicilio = this.changeListProvincia(this.lista_provincias, this.cliente_edit.datos_adicionales.domicilio.ubicacion_base.departamento);

            }

            if (!!this.$refs.mapEdit)
            { initMapEdit(this.cliente_edit.datos_adicionales.domicilio.ubicacion_gps); }
            */

          this.modal.editarCliente.modal("show");
        },
        function(responseError) {
          console.log(responseError);
        }
      );
    },

    loadProvincias: function() {
      //this.setListaProvincias();
      key_departamento = null;
      if (LEVEL == "L2") {
        console.log("Provincias nivel 2");
        key_departamento = this.clienteL2.lugar_nacimiento.departamento;
        this.clienteL2.lugar_nacimiento.ciudad_comunidad = null;
      }
      if (LEVEL == "L3") {
        console.log("Provincias nivel 3");
        key_departamento = this.clienteL3.lugar_nacimiento.departamento;
        this.clienteL3.lugar_nacimiento.ciudad_comunidad = null;
      }

      if (!!key_departamento) {
        this.provincias = this.changeListProvincia(
          this.lista_provincias,
          key_departamento
        );
      } else {
        console.log("ERROR de cargado de provincias");
      }
    },

    loadProvinciasDomicilio: function() {
      //this.setListaProvincias();
      key_departamento = null;
      if (LEVEL == "L3") {
        console.log("Provincias nivel 3");
        //key_departamento = this.clienteL3.datos_adicionales.domicilio.ubicacion_base.departamento;
        //this.clienteL3.datos_adicionales.domicilio.ubicacion_base.ciudad_comunidad = null;
      }

      if (!!key_departamento) {
        //this.provincias = this.changeListProvincia(this.lista_provincias, key_departamento)
        this.provincias_domicilio = this.changeListProvincia(
          this.lista_provincias,
          key_departamento
        );
      } else {
        console.log("ERROR de cargado de provincias");
      }
    },

    changeListProvincia: function(lista_provincias, key_departamento) {
      // Generando lista filtrada de provincias segun el departamento seleccionado
      const provincias = [];
      for (item in lista_provincias) {
        key_prov = lista_provincias[item][0];
        //console.log(kew_prov)
        if (key_prov > key_departamento && key_prov <= key_departamento + 99) {
          //console.log(lista[item]);
          provincias.push(lista_provincias[item]);
        }
      }
      //console.log(provincias);
      return provincias;
    },
    setListaProvincias: function() {
      /*
       * Prepara una lista de provincias para que tenga el formato adecuado
       * para cargar en el select de provincias
       */
      var prov = PROVINCIAS;
      var provincias = [];
      for (item in prov) {
        tupla = PROVINCIAS[item].replace("'", "").replace("'", "").split(",");
        tupla[0] = parseInt(tupla[0]);
        //console.log(tupla)
        provincias.push(tupla);
      }
      //console.log("Provincias filtradas", provincias.length);
      this.lista_provincias = provincias;
    },
    loadListProvincias: function(is_actividad) {
      this.setListaProvincias();
      /*
                              if(is_actividad=="actividad"){
                                  this.provincias = this.changeListProvincia(this.lista_provincias, this.actividad_economica.ubicacion.departamento);
                              }else if(is_actividad=="conyuge"){
                                  this.provincias = this.changeListProvincia(this.lista_provincias, this.conyuge.lugar_nacimiento.departamento);
                              }else if(is_actividad == "edit_lugar_nacimiento"){
                                  console.log("Cargando provincias de modal edit cliente LN")
                                  this.cliente_edit.lugar_nacimiento.ciudad_comunidad = null;
                                  this.cliente_edit.lugar_nacimiento.provincia = null;
                                  this.provincias = this.changeListProvincia(this.lista_provincias, this.cliente_edit.lugar_nacimiento.departamento);
                              }else if(is_actividad == "edit_domicilio"){
                                  this.cliente_edit.datos_adicionales.domicilio.ubicacion_base.ciudad_comunidad = null;
                                  this.cliente_edit.datos_adicionales.domicilio.ubicacion_base.provincia = null;
                                  this.provincias_domicilio = this.changeListProvincia(this.lista_provincias, this.cliente_edit.datos_adicionales.domicilio.ubicacion_base.departamento);
                              }else if(is_actividad == "domicilio"){
                                  this.provincias = this.changeListProvincia(this.lista_provincias, this.clienteL3.datos_adicionales.domicilio.departamento)
                              }else{
                                  this.provincias = this.changeListProvincia(this.lista_provincias, this.referencia_personal.radicatoria.departamento);
                              }
                              */
    },
    // >> Carga lista de ciudades o comunidades en Typehead para cliente L2 y L3
    loadCiudadComunidad: function() {
      console.log("Cargando ciudades o comunidades");
      var url = URLS.endpoints.ciudadComunidad();
      self = this;
      this.ciudades = [];
      ciudades = [];
      if (LEVEL == "L2") {
        data = this.clienteL2.lugar_nacimiento;
        //this.clienteL2.lugar_nacimiento.ciudad_comunidad = null;
      }
      if (LEVEL == "L3") {
        data = this.clienteL3.lugar_nacimiento;
        //this.clienteL3.lugar_nacimiento.ciudad_comunidad = null;
      }

      this.$http.get(url, { params: data }).then(
        function(response) {
          ciudades = response.body;
          for (item in ciudades) {
            ciudades[item] = ciudades[item].ciudad_comunidad;
          }
          //console.log(ciudades)
          this.ciudades = ciudades;
          KTTypeahead.init(this.ciudades);
        },
        function(responseError) {
          //console.log("ERROR", responseError);
          this.ciudades = [];
          //KTTypeahead.init(this.ciudades);
        }
      );
    },
    // >> Carga lista de ciudades o comunidades en Typehead de Actividad economica (modal)
    loadCiudadComunidadActividadReferencia: function(is_actividad) {
      var url = URLS.endpoints.ciudadComunidad();
      self = this;
      this.ciudades = [];
      ciudades = [];
      this.ciudades_edit = [];
      ciudades_edit = [];
      /*if(is_actividad=="actividad"){
                                  data = this.actividad_economica.ubicacion;
                                  this.actividad_economica.ubicacion.ciudad_comunidad = null;
                              }else if(is_actividad=="conyuge"){
                                  data=this.conyuge.lugar_nacimiento;
                                  this.conyuge.lugar_nacimiento.ciudad_comunidad = null;

                              }else if(is_actividad=="edit_lugar_nacimiento"){
                                  data=this.cliente_edit.lugar_nacimiento;
                                  this.cliente_edit.lugar_nacimiento.ciudad_comunidad = null;

                              }else if(is_actividad=="edit_domicilio"){
                                  data=this.cliente_edit.datos_adicionales.domicilio;
                                  this.cliente_edit.datos_adicionales.domicilio.ciudad_comunidad = null;
                              }else if(is_actividad=="domicilio"){
                                  data=this.cliente_edit.datos_adicionales.domicilio;
                                  this.cliente_edit.datos_adicionales.domicilio.ciudad_comunidad = null;

                              }else{
                                  data=this.referencia_personal.radicatoria;
                                  this.referencia_personal.radicatoria.ciudad_comunidad = null;
                              }

                              this.$http.get(url, { 'params': data }).then(
                                  function(response) {
                                      ciudades = response.body;
                                      for (item in ciudades) {
                                          ciudades[item] = ciudades[item].ciudad_comunidad
                                      }
                                      if(is_actividad=="edit_domicilio"){
                                          this.ciudades_edit = ciudades;
                                          UbicacionActividadReferenciaTypeahead.init(this.ciudades);
                                      } else{
                                          this.ciudades = ciudades;
                                          UbicacionActividadReferenciaTypeahead.init(this.ciudades);
                                      }
                                      //UbicacionReferenciaPersonalTypeahead.init(this.ciudades);
                                  },
                                  function(responseError) {
                                      //console.log("ERROR", responseError);
                                      this.ciudades = [];

                                  }
                                  );
                                  */
    },
    // >> Carga lista de ciudades o comunidades en Typehead de domicilio para L2 y L3
    /*

                    loadCiudadComunidadDomicilio: function() {
                        //console.log("Cargando ciudades o comunidades");
                        var url = URLS.endpoints.ciudadComunidad();
                        self = this;
                        this.ciudades = [];
                        ciudades = [];
                        if (LEVEL == "L2") {
                            data = this.clienteL2.lugar_nacimiento;
                            this.clienteL2.lugar_nacimiento.ciudad_comunidad = null;
                        }
                        if (LEVEL == "L3") {
                            data = this.clienteL3.datos_adicionales.domicilio;
                            this.clienteL3.datos_adicionales.domicilio.ciudad_comunidad = null;
                        }

                        this.$http.get(url, { 'params': data }).then(
                            function(response) {
                                ciudades = response.body;
                                for (item in ciudades) {
                                    ciudades[item] = ciudades[item].ciudad_comunidad
                                }
                                //console.log(ciudades)
                                this.ciudades = ciudades;
                                DomicilioTypeahead.init(this.ciudades);
                            },
                            function(responseError) {
                                //console.log("ERROR", responseError);
                                this.ciudades = [];
                                //KTTypeahead.init(this.ciudades);

                            }
                            );

                        },
                        filtrarActividades: function(clave){
                            //console.log("Cargando actividades", this.actividad_economica.actividad)
                            // Caragando la lista de actividades
                            //var url = URLS.endpoints.activities(this.actividad_economica.actividad);

                            var url = URLS.endpoints.activities2(clave);

                            this.$http.get(url).then(
                                function(response) {
                                    this.actividades = response.body;
                                    //console.log("******", this.actividades);
                                    ActividadTypeahead.init(this.actividades);
                                    //console.log(response)
                                },
                                function(responseError) {
                                    console.log("ERROR");
                                    console.log(responseError);
                                }
                                );
                            },
                            */
    /*
                    loadActividades: function(){
                        //console.log("****** Cargando actividades economicas ******")
                        /**
                        var url = URLS.endpoints.activities();
                        this.$http.get(url).then(
                            function(response) {
                                this.actividades = response.body;
                                //console.log("******", this.actividades);
                                ActividadTypeahead.init(this.actividades)
                            },
                            function(responseError) {
                                console.log("ERROR");
                                console.log(responseError);
                            }
                            );

                        },
                        agregarActividadEconomica: function(){
                            console.log("********** Crear Actividad **********");
                            url = URLS.endpoints.addActivities();
                            var _header = { headers: { "X-CSRFToken": csrftoken } };
                            var data = this.actividad_economica;
                            this.$http.post(url, data, _header).then(
                                function(response) {
                                    this.actividades = response.body;
                                    //this.cliente = response.body;
                                    console.log("ACTIVIDAD ECONOMICA ALMACENADO", response);
                                    toastr.success("Se ha almacenado correctamente la actividad económica", "<h6>Almacenado correctamente</h6>");
                                    //ActividadTypeahead.init(this.actividades)
                                    this.modal.adicionarActividadEconomica.modal('hide');
                                },
                                function(responseError) {
                                    console.log("ERROR");
                                    console.log(responseError);
                                }
                                );
                            },
                            agregarReferenciaPersonal: function(){
                                console.log("********** Crear Referencia Personal **********");
                                url = URLS.endpoints.addReference();
                                var _header = { headers: { "X-CSRFToken": csrftoken } };
                                var data = this.referencia_personal;
                                this.$http.post(url, data, _header).then(
                                    function(response) {
                                        this.referencias = response.body;
                                        //this.cliente = response.body;
                                        console.log("REFERENCIA PERSONAL ALMACENADO", response);
                                        toastr.success("Se ha almacenado correctamente la referencia personal", "<h6>Almacenado correctamente</h6>");
                                        //ActividadTypeahead.init(this.actividades)
                                        this.modal.adicionarReferenciaPersonal.modal('hide');
                                    },
                                    function(responseError) {
                                        console.log("ERROR");
                                        console.log(responseError);
                                    }
                                    );
                                },
                                agregarConyuge: function(){
                                    console.log("********** Crear CONYUGE **********");
                                    url = URLS.endpoints.addSpouse();
                                    var _header = { headers: { "X-CSRFToken": csrftoken } };
                                    var data = this.conyuge;
                                    this.$http.post(url, data, _header).then(
                                        function(response) {
                                            this.conyuges = response.body;
                                            //this.cliente = response.body;
                                            //console.log("CONYUGE ALMACENADO", response);
                                            toastr.success("Se ha almacenado correctamente la conyuge", "<h6>Almacenado correctamente</h6>");
                                            //ActividadTypeahead.init(this.actividades)
                                            this.modal.adicionarConyuge.modal('hide');
                                        },
                                        function(responseError) {
                                            console.log("ERROR");
                                            console.log(responseError);
                                        }
                                        );
                                    },
                                    deleteCliente:function(pk){
                                        var url = URLS.endpoints.deleteCliente(pk);
                                        console.log("Eliminando cliente", pk, url);
                                        var _header = { headers: { "X-CSRFToken": csrftoken } };
                                        var self = this;
                                        Swal.fire({
                                            title: "¿Está seguro?",
                                            text: "Se eliminara el cliente y todos sus datos.",
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
                                                console.log("eliminando nuevo cliente...")
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
                                        editCliente:function(pk){
                                            var url = URLS.endpoints.deleteCliente(pk);
                                            console.log("Eliminando cliente", pk, url);
                                            var self = this;
                                            Swal.fire({
                                                title: "¿Está seguro?",
                                                text: "Se actualizaran los datos del clinete.",
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
                                                self.saveEditCiente(pk)
                                            });


                                        },
                                        */
  },
  mounted: function() {
    actividadTimepicker.init();
    actividad2Timepicker.init();
    //console.log("Cargando Lista de clientes");
    //KTGoogleMapsDemo.init();
    //KTFormControls.init();
    /*
    this.modal.adicionarClienteL1 = $(this.$refs.adicionarModalClienteL1);
    this.modal.editarCliente = $(this.$refs.editModalCliente);
    this.modal.adicionarConyugue = $(this.$refs.adicionarModalConyugue);
    this.modal.adicionarActividadEconomica = $(this.$refs.adicionarModalActividadEconomica);
    this.modal.adicionarReferenciaPersonal = $(this.$refs.adicionarModalReferenciaPersonal);
    */
    //this.modal.adicionarConyugue.modal('show');
    //this.modal.adicionarActividadEconomica.modal('show');
    //this.modal.editarCliente.modal('show')

    this.loadListClientes();
    this.filterCiudades(this.domicilio.ubicacion.departamento, "domicilio");
    //this.setListaProvincias()
    //this.loadActividades();
    //this.loadListProvincias();
    //this.loadCiudadComunidadActividadReferencia();

    //DatepickerNacimiento.init();
    //DatepickerVigencia.init();
    //DatepickerConyuge.init();
    //TimepickerActividadEconomica.init();
    //KTContactsAdd.init();
    //KTTagifyDias.init();

    if (!!this.$refs.map) {
      initMap();
    }

    if (!!this.$refs.map_domicilio) {
      initMapDomicilio();
    }
    if (!!this.$refs.map_conyuge) {
      initMapConyuge();
    }
    if (!!this.$refs.map_actividad) {
      initMapActividad();
    }
    if (!!this.$refs.map_actividad_secundaria) {
      initMapActividadSecundaria();
    }
  },
});