var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
const RELACION_FAMILIAR = [
  {'key': 'HE', 'value': 'Hermano(a)'},
  {'key': 'PA', 'value': 'Padre'},
  {'key': 'MA', 'value': 'Madre'},
  {'key': 'HI', 'value': 'Hijo(a)'},
  {'key': 'CU', 'value': 'Cuñado(a)'},
  {'key': 'SU', 'value': 'Suegro(a)'},
  {'key': 'PR', 'value': 'Primo(a)'},
];
const RELACION_PERSONAL = [
  {'key': 'CT', 'value':'Compañero de trabajo'},
  {'key': 'Ve', 'value':'Vecino'},
  {'key': 'DC', 'value':'Dueño de casa'},
  {'key': 'AM', 'value':'Amistad'},
  {'key': 'OT', 'value':'Otros'},
];
const CLIENTE = {
  codigo_cliente: null,
  tipo_persona: "N",
  codcli_alternativo: null,
  codigo_tipo_documento: null,
  valor_documento_identificacion: null,
  extension: null,
  estado_documento_identificacion: null,
  fecha_vencimiento_documento: null,
  codigo_ruc: null,
  apellido_paterno: null,
  apellido_materno: null,
  primer_nombre: null,
  segundo_nombre: null,
  apellido_esposo: null,
  nombre_completo: null,
  conocido_por: null,
  sexo_cliente: null,
  codigo_estado_civil: null,
  numero_dependientes: 0,
  lugar_nacimiento_cliente: null,
  fecha_nacimiento_cliente: null,
  nacionalidad_cliente: "BO",
  codigo_sector_social: null,
  correo_electronico_1: null,
  correo_electronico_2: null,
  telefono_movil_1: null,
  telefono_movil_2: null,
  ocupacion_cliente: null,
  secuencia_cliente: null,
  ultima_operacion: null,
  observaciones: null,
  fecha_inscripcion: null,
  codigo_motivo_cr: null,
  nivel_datos_cliente: null,
  socio_cooperativa: null,
  estado_cliente: null,
  id_citytroops: null,
  codigo_estado_civil_actual: null,
};
const CLIENTE_DATA = {
  codigo_cliente: 111,
  codigo_tipo_documento: 1,
  valor_documento_identificacion: "6541230",
  tipo_persona: "N",
  extension: "SE",
  apellido_paterno: "Chura",
  apellido_materno: null,
  primer_nombre: "Pedro",
  segundo_nombre: null,
  conocido_por: "Piter",
  sexo_cliente: "M",
  codigo_estado_civil: "S",
  numero_dependientes: 0,
  lugar_nacimiento_cliente: "El Alto - La Paz",
  nacionalidad_cliente: "BO",
  codigo_sector_social: 1,
  correo_electronico_1: "piter@mail.com",
  telefono_movil_1: "76543210",
  ocupacion_cliente: "Investigador criminal",
  codigo_motivo_cr: 1,
  nivel_datos_cliente: 3,
  codigo_estado_civil_actual: "S",
  fecha_nacimiento_cliente: "2000-01-01",
};
const DIRECCION = {
  codigo_registro: null,
  codigo_cliente: null,
  tipo_direccion: null,
  detalle_direccion: null,
  ubicacion_direccion: null,
  anios_residencia: null,
  telefono: null,
  codigo_tenencia: null,
  codigo_zona: null,
  codigo_area: null,
  estado_direccion: null,
  fecha_creacion: null,
  ultima_actualizacion: null,
  ultima_transferencia: null,
  oficina_actualizacion: null,
  usuario_actualizacion: null,
  comentario: null,
  numero_puerta: null,
  latitud: null,
  longitud: null,
};
const DIRECCION_DATA = {
  codigo_registro: 1222,
  codigo_cliente: 4,
  tipo_direccion: "D",
  detalle_direccion: "Este es el detalle de la direccion",
  ubicacion_direccion: "Esta es la ubicacion detallada",
  anios_residencia: 2,
  telefono: "76543210",
  codigo_tenencia: "F",
  codigo_zona: 101169,
  codigo_area: 12,
  estado_direccion: "V",
  comentario: "Este es un comentario adicional al registro",
  numero_puerta: "1255",
  latitud: -16.503796017651304,
  longitud: -68.16268515902941,
  tipo_direccion:"D",
  oficina_actualizacion: 101,
};
const CLIENTE_ACTIVIDAD = {
  codigo_registro: null,
  codigo_cliente: null,
  codigo_actividad: null,
  actividad_principal: null,
  anios_actividad: null,
  tipo_actividad: null,
  dias_actividad: ['L', 'M', 'X', 'J', 'V', 'S'],
  horario_actividad: null,
  ciclo_rotacion: 0,
  capital_rotacion: 0,
  estado_relacion: null,
  ultima_actualizacion: null,
  ultima_transferencia: null,
  oficina_actualizacion: null,
  usuario_actualizacion: null,
  ingreso_mensual_aproximado: null,
  tipo_ingreso: "I",
  ocupacion_cliente: null,
}
const CLIENTE_ACTIVIDAD_DATA = {
  descripcion_actividad: null,
  codigo_registro: 123123,
  codigo_cliente: "1010007125",
  codigo_actividad: 1223,
  actividad_principal: "V",
  anios_actividad: 5,
  tipo_actividad: "F",
  dias_actividad: ['L', 'M', 'X', 'J', 'V', 'S'],
  horario_actividad: null,
  ciclo_rotacion: 100,
  capital_rotacion: 100,
  estado_relacion: "V",
  ultima_actualizacion: "2022-01-01 10:10:10",
  ultima_transferencia: null,
  oficina_actualizacion: 10,
  usuario_actualizacion: 100,
  ingreso_mensual_aproximado: 4000,
  tipo_ingreso: "I",
  ocupacion_cliente: "Comerciante",
}
const ACTIVIDAD = {
  codigo_registro: null,
  codigo_actividad: null,
  descripcion_actividad: null,
  codigo_rubro: null,
  codigo_relacion: null,
  estado_actividad: null,
  oficina_actualizacion: null,
  usuario_actualizacion: null,
  ultima_actualizacion: null,
  ultima_transferencia: null,
}
const ACTIVIDAD_DATA = {
  codigo_registro: null,
  codigo_actividad: null,
  descripcion_actividad: "Esta es una descripcion de la actividad",
  codigo_rubro: null,
  codigo_relacion: null,
  estado_actividad: null,
  oficina_actualizacion: null,
  usuario_actualizacion: null,
  ultima_actualizacion: null,
  ultima_transferencia: null,
};
const REFERENCIA = {
  codigo_registro: null,
  codigo_cliente: null,
  nombre_referencias: null,
  direccion_referencias: null,
  ubicacion_referencias: null,
  relacion_referencias: null,
  telefono_referencias: null,
  estado_referencias: 'V',
  ultima_actualizacion: null,
  ultima_transferencia: null,
  oficina_actualizacion: 102,
  usuario_actualizacion: 101,
  tipo_referencia: null,
};
const REFERENCIA_DATA = {
  usuario_actualizacion: 101,
  oficina_actualizacion: 10,
  codigo_registro: "1012",
  codigo_cliente: null,
  nombre_referencias: "Marciano Terricola",
  direccion_referencias: "z. Mercedes, Av. La Paz, No. 123",
  ubicacion_referencias: "El Alto",
  relacion_referencias: "MA",
  telefono_referencias: "76543210", 
  tipo_referencia: "F",
};
const CONYUGE = {
  codigo_registro: null,
  codigo_cliente: null,
  apellido_paterno: null,
  apellido_materno: null,
  nombres: null,
  valor_documento_identificacion: null,
  extension: null,
  fecha_nacimiento: null,
  lugar_nacimiento: null,
  telefono_movil: null,
  ocupacion_conyugue: null,
  direccion_trabajo_negocio: null,
  fecha_creacion: null,
  estado_registro: null,
  ultima_actualizacion: null,
  oficina_actualizacion: null,
  usuario_actualizacion: null,
}
const CONYUGE_DATA = {
  codigo_registro: 1111,
  usuario_actualizacion: 100,
  codigo_cliente: null,
  apellido_paterno: "Mamani",
  apellido_materno: "Perez",
  nombres: "Maria Jacinta",
  valor_documento_identificacion: "6565656",
  extension: "LP",
  fecha_nacimiento: "1998-01-01",
  lugar_nacimiento: "Caranavi",
  telefono_movil: "74125630",
  ocupacion_conyugue: "Arquitecta",
  direccion_trabajo_negocio: "La Paz, av. Buenos Aires, No. 23",
  fecha_creacion: "2022-01-01 10:10:10",
  estado_registro: "V",
  ultima_actualizacion: "2022-01-01 10:10:10",
  oficina_actualizacion: 10
}
let app = new Vue({
  el : "#kt_content_cliente",
  data : {
    modal: {
      adicionarDireccion: null,
      adicionarActividad: null,
    },
    control: "select2",
    zona: null,
    index: -1,
    index_actividad: -1,
    index_referencia: -1,
    dias_actividad: ['L', 'M', 'X', 'J', 'V', 'S'],
    hora_inicial: "08:00",
    hora_final: "18:00",
    lista_actividades: [],
    lista_tenencias: [],
    lista_zonas: [],
    codigo_actividad: null,
    relacion_familiar: RELACION_FAMILIAR,
    relacion_personal: RELACION_PERSONAL,
    direccion: DIRECCION,
    cliente: CLIENTE,    
    actividad: CLIENTE_ACTIVIDAD, 
    cliente_actividad: {...CLIENTE_ACTIVIDAD},
    referencia: {...REFERENCIA},
    conyuge: {...CONYUGE},
    direcciones:[],
    actividades:[],
    referencias:[],
    cliente_guardado: false,
    select:{
      zona: null,
      actividad: null,
    },
    load: false,
    conyuge_data: {},
  },
  computed: {
    'actividad.descripcion_actividad': function() {
      descripcion = this.lista_actividades.map(item => {
        if(item.codigo_actividad == this.actividades[index_actividad].codigo_actividad) {
          return item.descripcion_actividad;
        }
      })
    },
    tipo_actividad: function() {
      return (tipo) => tipo=='F' ? 'Fijo' : 'Ambulante';
    },
    tipo_ingreso: function() {
      return (tipo) => tipo=='I' ? 'Independiente' : tipo=='D' ? 'Dependiente' : 'No Aplica';
    },
    tipo_relacion_personal: function() {
      return (key) => RELACION_PERSONAL.find( (item) => item.key===key ).value;
    },
    tipo_relacion_familiar: function() {
      return (key) => RELACION_FAMILIAR.find( (item) => item.key===key ).value;
    },
    tipo_referencia: function() {
      return (tipo) => tipo=='F' ? 'Familiar' : 'Personal';
    },
  },
  watch: {
    "cliente.codigo_estado_civil_actual": function(newValue, oldValue) {
      if(newValue == 'C' || newValue == 'N') {
        console.log("Cambio de estado civil", newValue, oldValue);
        if(this.load) {
          this.conyuge = this.conyuge_data;
        }
        else{
          this.conyuge = {...CONYUGE};
        }
      }
    }
  },
  methods : {
    
    filterZonasByDescriptions: function(key){
      let url = URLS.endpoints.filterZonas(key);
      this.lista_zonas = this.getList(url);
      console.log("Lista actividades: ", url, this.lista_zonas);
    },

    listZonas: function(){
      let url = URLS.endpoints.listZonas();
      this.$http.get(url).then(
        function(response) {
          this.lista_zonas = response.body;
        },
        function(responseError) {
          console.log("ERROR", responseError);
          lista = responseError;
        }
      );
    },

    filterActividadesByDescription: function(key){
      let url = URLS.endpoints.actividadDescripcion(key);
      this.$http.get(url).then(
        function(response) {
          console.log("Lista actividades: ", response.body);
          this.lista_actividades = response.body;
          TypeaheadActividad.init(this.lista_actividades);
        },
        function(responseError) {
          console.log("ERROR", responseError);
          lista = responseError;
        }
      );
    },
    
    listActividades: function(){
      let url = URLS.endpoints.listActividades();
      
      this.$http.get(url).then(
        function(response) {
          this.lista_actividades = response.body;
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
      
    },
    listTenencias: function(){
      let url = URLS.endpoints.listTenencias();
      console.log("Buscando tenencia: ", url);
      this.$http.get(url).then(
        function(response) {
          this.lista_tenencias = response.body;
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },

    editFichaDatos : function(){
      let url = URLS.endpoints.editFichaDatos(this.cliente.codigo_cliente);
      console.log("EDITANDO FICHA DE DATOS", url, this.conyuge);
      this.preSaveFichaDatos();

      let data = {};
      if (this.cliente){
        data['cliente'] = this.cliente;
        if (this.conyuge && this.cliente.codigo_estado_civil_actual == 'C' || this.cliente.codigo_estado_civil_actual == 'N'){
          data['conyuge'] = this.conyuge;
        }    
      }  
      if (this.actividades){
        data['actividades'] = this.actividades;
      }    
      if (this.direcciones){
        data['direcciones'] = this.direcciones;
      }    
      if (this.referencias){
        data['referencias'] = this.referencias;
      }    
      let self = this;
      this.$http.put(url, data, csrf_token).then(
        function(response) {
          console.log("PUT RESPONSE: ", response.body);
          let message = response.body.cliente_created.codigo_cliente+" "+response.body.cliente_created.primer_nombre+" "+response.body.cliente_created.apellido_paterno;
          toastr.success(message, "Cliente editado!");
          if (!!response.body.cliente){ self.cliente = response.body.cliente;}
          if (!!response.body.conyuge){ self.conyuge = response.body.conyuge;}
          if (!!response.body.actividades){ self.actividades = response.body.actividades;}
          if (!!response.body.direcciones){ self.direcciones = response.body.direcciones;}
          if (!!response.body.referencia){ self.referencias = response.body.referencias;}

        },
        function(responseError) {
          console.log("ERROR ", responseError.body);
          if (!!responseError.body){
            for(error in responseError.body){
              let array_error = responseError.body[error];
              for(error_item in array_error){
                toastr.error(array_error[error_item].message, error);
              } 
            }
          }
        }
      );
    },

    listFichaDatos : function(){
      let url = URLS.endpoints.fichaDatos();
      console.log("LISTA FICHA DE DATOS", url);

      this.$http.get(url).then(
        function(response) {
          console.log(response.body);
          toastr.success("Lista cargada!");
        },
        function(responseError) {
          console.log("ERROR ", responseError.body);
        }
      );
    },

    saveFichaDatos : function(){
      let url = URLS.endpoints.fichaDatos();
      console.log("CREANDO FICHA DE DATOS", url);
      this.preSaveFichaDatos();

      let data = {
        cliente: this.cliente,
        actividades: this.actividades,
        conyuge: this.conyuge,
        direcciones: this.direcciones,
        referencias: this.referencias,
      };

      this.$http.post(url, data, csrf_token).then(
        function(response) {
          console.log(response.body);
          let message = response.body.cliente_created.codigo_cliente+" "+response.body.cliente_created.primer_nombre+" "+response.body.cliente_created.apellido_paterno;
          toastr.success(message, "Cliente creado!");
        },
        function(responseError) {
          console.log("ERROR ", responseError.body);
          if (!!responseError.body){
            for(error in responseError.body){
              let array_error = responseError.body[error];
              for(error_item in array_error){
                toastr.error(array_error[error_item].message, error);
              } 
            }
          }
        }
      );
    },
    preSaveFichaDatos : function(){
      console.log("PRE-SAVE FICHA DE DATOS", this.cliente.fecha_nacimiento_cliente);
      if (this.cliente.fecha_nacimiento_cliente != null && this.cliente.fecha_nacimiento_cliente.length <= 10 ) {
        this.cliente.fecha_nacimiento_cliente = this.cliente.fecha_nacimiento_cliente+'T00:00';
      }
      
    },
    saveCliente : function(){
      let url = URLS.endpoints.clientes();
      //console.log("Guardadndo cliente", this.cliente, url);
      this.cliente.fecha_nacimiento = new Date(this.cliente.fecha_nacimiento)

      this.$http.post(url, this.cliente, csrf_token).then(
        function(response) {
          this.cliente_guardado = true;
          this.cliente = response.body;
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    loadFichaDatos : function(codigo_cliente){
      let url = URLS.endpoints.getFichaDatos(codigo_cliente);
      let self = this;
      this.$http.get(url).then(
        function(response) {
          console.log("GET RESPONSE: ", response.body);
          if (!!response.body.cliente){ self.cliente = response.body.cliente;}
          if (!!response.body.conyuge && self.cliente.codigo_estado_civil_actual=='C'|| self.cliente.codigo_estado_civil_actual=='N'){
            console.log("CONYUGE cargado", response.body.conyuge);
            self.conyuge = {...response.body.conyuge};
            self.conyuge_data = response.body.conyuge;
          }
          if (!!response.body.actividades){ self.actividades = response.body.actividades;}
          if (!!response.body.direcciones){ self.direcciones = response.body.direcciones;}
          if (!!response.body.referencia){ self.referencias = response.body.referencias;}
          this.load = true;
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    saveDirecciones : function(){
      let url = URLS.endpoints.saveDirecciones();
      console.log("Guardadndo direcciones", this.direcciones, url);
      let data = { 'direcciones': this.direcciones };
      this.$http.post(url, data, csrf_token).then(        
        function(response) {
          console.log(response.body)
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    saveActividades: function(){
      let url = URLS.endpoints.saveActividades();
      console.log("Guardadndo actividades", this.actividades, url);
      let data = this.actividades;
      this.$http.post(url, data, csrf_token).then(
        
        function(response) {
          console.log(response.body)
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    saveReferencias: function(){
      let url = URLS.endpoints.saveRefererencias();
      console.log("Guardadndo referencias", this.referencias, url);
      let data = this.referencias;
      this.$http.post(url, data, csrf_token).then(
        
        function(response) {
          console.log(response.body)
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    saveconyuge: function(){
      let url = URLS.endpoints.saveConyuge();
      console.log("Guardadndo conyuge", this.conyuge, url);
      let data = this.conyuge;
      this.$http.post(url, data, csrf_token).then(
        
        function(response) {
          console.log(response.body)
        },
        function(responseError) {
          console.log("ERROR");
          console.log(responseError);
        }
      );
    },
    deleteDireccionToArray: function(index){
      console.log("Eliminando Direccion", index);
      this.direcciones.splice(index, 1);
    },
    deleteReferenciaToArray: function(index){
      console.log("Eliminando referencia", index);
      this.referencias.splice(index, 1);
    },
    deleteActividadToArray: function(index){
      console.log("Eliminando referencia", index);
      this.actividades.splice(index, 1);
    },
    openModalDireccion: function(){
      console.log("Abrir modal");
      this.modal.adicionarDireccion.modal('show');
    },
    openModalEditDireccion: function(direccion, index){
      console.log("Abrir modal edicion");
      this.index = index;
      this.direccion = {...direccion};
      this.openModalDireccion();
    },
    openModalEditActividad: function(actividad, index){
      console.log("Abrir modal edicion actividad", actividad);
      this.index_actividad = index;
      this.actividad = {...actividad};
      this.openModalActividad();
    },
    editReferencia: function(referencia, index){
      console.log("Abrir modal edicion actividad", referencia);
      this.index_referencia = index;
      this.referencia = {...referencia};
    },
    openModalActividad: function(){
      console.log("Abrir modal");
      this.modal.adicionarActividad.modal('show');
    },
    addDireccionToArray: function(){
      console.log("Agregando direccion", this.index);
      if( this.index >= 0 ){
        console.log("Editando direccion", this.direcciones[this.index]);
        this.direcciones.splice(this.index, 1, this.direccion);
        console.log("Nueva direccion", this.direcciones[this.index]);
      } else{
        this.direcciones.push({...this.direccion});
        this.direccion = {...DIRECCION_DATA};
      }
      this.index = -1;
      this.modal.adicionarDireccion.modal('hide');
    },
    addActividadToArray: function(){
      this.actividad.horario_actividad = this.hora_inicial + " - " + this.hora_final;
      this.actividad.dias_actividad = this.dias_actividad.join("");
      
      if( this.index_actividad >= 0 ){
        this.actividades.splice(this.index, 1, this.actividad);
      } else{
        //this.hora_inicial = this.hora_final = "00:00";

        this.actividades.push({...this.actividad});
        this.actividad = {...CLIENTE_ACTIVIDAD};
      }
      this.index_actividad = -1;

      this.modal.adicionarActividad.modal('hide');
    },
    addReferenciaToArray: function(){
      // TODO: Validar los datos enviados y que todos los inputs esten llenos
      console.log("Agregando referencia", this.referencias);
      if(this.index_referencia >= 0){
        // Actualizar datos en el array
        this.referencias.splice(this.index, 1, this.referencia);
        this.referencia = REFERENCIA;
      } else{
        // Agregar nuevos datos en el array
        this.referencias.push({...this.referencia});
        this.referencia = REFERENCIA;
      }
      this.index_referencia = -1;
    },
    saveClienteCompleto: function(){
      console.log("Guardando cliente completo");
      this.saveCliente();
    },
  },
  mounted : function(){
    this.modal.adicionarDireccion = $(this.$refs.modalAdicionarDireccion);
    this.modal.adicionarActividad = $(this.$refs.modalAdicionarActividad);
    this.select.actividad = $(this.$refs.selectActividad);
    this.select.zona = $(this.$refs.selectZona);
    //console.log("prueba de carga MOUNTED");
    //this.modal.adicionarActividad.modal('show');
    //this.openModalActividad();
    this.listTenencias();
    this.listActividades();
    this.listZonas();
    //this.addDireccionToArray();
    if(CLIENTE_EDIT){
      console.log("Editando cliente", CLIENTE_EDIT);
      this.loadFichaDatos(CLIENTE_EDIT);
    } else {
      console.log("Nuevo cliente");
    }
  }
});
