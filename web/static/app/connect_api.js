var URLS = {
  endpoints: {
    // -------------- URLS HOME --------------
    urlFormularioComplemento: function(slug) {
      return "https://jgp.com.bo/solicitud/" + slug + "/";
    },
    // -------------- URLS USER --------------
    enclosure: function(slug) {
      return "/api/v1/" + slug + "/";
    },
    peopleName: "{% url 'api-control:v1:peopleName' %}",
    getProfile: function() {
      return "/api/v1/me/profile/";
    },
    putProfile: function() {
      return "/api/v1/me/profile/";
    },
    putPassword: function() {
      return "/api/v1/me/password/";
    },
    getUsers: function() {
      return "/api/v1/users/";
    },
    getAssesor: function(user) {
      return "/api/v1/solicitud/asesor/estadisticas/"+user+"/";
    },
    // -------------- URLS EMPRESA --------------
    getSucursales: function() {
      return "/api/v1/empresa/sucursales/";
      
    },

    // -------------- URLS FICHA DE DATOS --------------
    fichaDatos: function() {
      return "/api/v1/ficha-datos/";
    },
    editFichaDatos: function(codigo) {
      return "/api/v1/ficha-datos/"+codigo+"/";
    },
    getFichaDatos: function(codigo) {
      return "/api/v1/ficha-datos/"+codigo+"/";
    },
    // -------------- URLS CLIENTE --------------
    clientes: function() {
      return "/api/v1/clientes/";
    },
    listTenencias: function() {
      return "/api/v1/tenencias/";
    },
    saveDirecciones: function() {
      return "/api/v1/direcciones/";
    },
    saveRefererencias: function() {
      return "/api/v1/referencias-personales/";
    },
    saveConyuge: function() {
      return "/api/v1/conyuges/";
    },
    saveActividades: function() {
      return "/api/v1/actividades-economicas/";
    },
    // -------------- URLS ZONAS --------------
    listZonas: function() {
      return "/api/v1/zonas/";
    },
    filterZonas: function(value) {
      return "/api/v1/zonas/descripcion/"+value+"/";
    },
    // -------------- URLS ACTIVIDAD --------------
    listActividades: function() {
      return "/api/v1/actividades/";
    },
    actividadCodigo: function(value) {
      return "/api/v1/actividad/codigo/"+value+"/";
    },
    actividadDescripcion: function(value) {
      return "/api/v1/actividad/descripcion/"+value+"/";
    },
    createFichaDatos: function(value) {
      return "/api/v1/clientes/create/";
    },

    //------------------REPORTES------------------
    getReporteData: function(){
      return "http://190.181.25.202:8000/api/v1/cre/rep/creditos_enmora/Activa/101/110/0/0"

      //return "/api/v1/empresa/sucursales/";
    },
    //------------------DEPOSITOSV2------------------
    getDepositoData: function(){
      return "http://190.181.25.202:8000/api/v1/cre/rep/detalle_cobranza/0/0"

      //return "/api/v1/empresa/sucursales/";
    },
    /*
    getCliente: function(pk) {
        return "/api/v1/cliente/" + pk + "/";
    },
    deleteCliente: function(pk) {
        return "/api/v1/cliente/delete/" + pk + "/";
    },
    clientAddL1: function() {
        return "/api/v1/clientes/level1/";
    },
    clientAddL2: function() {
        return "/api/v1/clientes/level2/";
    },
    clientAddL3: function() {
        return "/api/v1/clientes/level3/";
    },
    provincias: function(code) {
        return "/api/v1/clientes/provincias/" + code + "/";
    },
    ciudadComunidad: function() {
        return "/api/v1/clientes/ciudad-coumunidad/";
    },
    ciudadComunidadDomicilio: function() {
        return "/api/v1/clientes/ciudad-coumunidad-domicilio/";
    },
    // -------------- URLS CLIENTE -------------
    activities2: function(clave) {
        return "/api/v1/clientes/actividades/" + clave + "/";
    },
    activities: function() {
        return "/api/v1/clientes/actividades/";
    },
    addActivities: function() {
        return "/api/v1/clientes/actividad/crear/";
    },
    */

    // -------------- URLS DEPOSITO --------------
    
    crearListarDeposito: function() {
      return "/api/v1/depositos/";
    },
    listbanco: function() {
      return "/api/v1/depositos/obtener/";
    },
    deleteDeposito: function(pk) {
      return "/api/v1/deposito/delete/" + pk + "/";
    },
    getEditDeposito: function(pk) {
      return "/api/v1/deposito/edit/" + pk + "/";
    },

    getVerificarDeposito: function(pk) {
      return "/api/v1/deposito/verificar/" + pk + "/";
    },

    getAplicadoDeposito: function(pk) {
      return "/api/v1/deposito/aplicado/" + pk + "/";
    },

    addReference: function() {
      return "/api/v1/clientes/referencia/crear/";
    },
    addSpouse: function() {
      return "/api/v1/clientes/conyuge/crear/";
    },
    // -------------- URLS UBICACION -------------
    ubicacionNacimiento: function(pk) {
      return "/api/v1/clientes/ubicacion/nacimiento/" + pk + "/";
    },
    ubicacionVivienda: function(pk) {
      return "/api/v1/clientes/ubicacion/vivienda/" + pk + "/";
    },
    ubicacionFilterCity: function() {
      return "/api/v1/solicitud/ciudad/filter/";
    },
    ubicacionProvinciaFilterCity: function() {
      return "/api/v1/solicitud/provincia/ciudad/filter/";
    },
    ubicacionFilterZone: function() {
      return "/api/v1/solicitud/zona/filter/";
    },
    // -------------- URLS ACTIVOS -------------
    getActivoFijo: function(id) {
      return "/api/v1/activo-fijo/" + id + "/";
    },
    putActivoFijo: function(id) {
      return "/api/v1/activo-fijo/" + id + "/";
    },
    getImagenActivoFijo: function(id) {
      return "/api/v1/activo-fijo/imagen/" + id + "/";
    },
    postActivoFijo: function(id) {
      return "/api/v1/activo-fijo/crear/";
    },
    getListActivoFijo: function(id) {
      return "/api/v1/activo-fijo/lista/";
    },
    findActivoFijo: function(id) {
      return "/api/v1/activo-fijo/filtrar/";
    },

    // -------------- URLS CERTIFICADOS -------------
    certifAdd: function() {
      return "/api/v1/certificados/crear/";
    },
    certif: function() {
      return "/api/v1/certificados/";
    },
    postCertificado: function() {
      return "/api/v1/certificados/crear/";
    },
    getClienteCertificado: function(pk) {
      //return "http://190.181.25.202:8001/api/cliente/certificado/"+pk;
      return "https://api.jesusgranpoder.com.bo/api/clientes/datos-certificado/" + pk ;
    },
    getAccess: function() {
      //return "http://190.181.25.202:8001/api/cliente/certificado/"+pk;
      //return "https://api.jesusgranpoder.com.bo/api/login?email=admin@jgp.com.bo&password=eM2QU8%26kFxZL";
      return "/api/v1/certificado/acceso/";
    },
    getCertificado: function(pk) {
      return "/api/v1/certificado/" + pk + "/";
    },
    deleteCertificado: function(pk) {
      return "/api/v1/certificado/delete/" + pk + "/";
    },
    editCertificado: function(slug) {
      return "/api/v1/certificado/edit/" + slug + "/";
    },

    // -------------- URLS FOTOS ACTIVOS -------------
    fotoActivoAddList: function(pk) {
      return "/api/v1/activo/" + pk + "/fotos/";
    },
    fotoActivoGetDelete: function(id_activo, id_foto) {
      return "/api/v1/activo/" + id_activo + "/fotos/" + id_foto + "/";
    },

    // -------------- URLS SOLICITUD CREDITO -------------
    ListCreateCredito: function() {
      return "/api/v1/solicitud/credito/";
    },
    createSolicitudComplemento: function(slug) {
      return "/api/v1/solicitud/credito/" + slug + "/";
    },
    createSolicitudDocumentos: function() {
      return "/api/v1/solicitud/credito/complemento/documentos/";
    },
    getSolicitud: function(slug) {
      return "/api/v1/solicitud/" + slug + "/";
    },
    deleteSolicitud: function(slug) {
      return "/api/v1/solicitud/eliminar/" + slug + "/";
    },
    updateSolicitud: function(slug) {
      return "/api/v1/solicitud/editar/" + slug + "/";
    },
    createSolicitudFotos: function(slug) {
      return "/api/v1/solicitud/" + slug + "/fotos/";
    },
    assignAdviser: function(slug) {
      return "/api/v1/solicitud/"+slug+"/asignar/asesor/";
    },
    unassignAdviser: function(slug) {
      return "/api/v1/solicitud/"+slug+"/desasignar/asesor/";
    },
    
    // -------------- URLS CONTRATO -------------
    contratAdd: function() {
      return "/api/v1/contrato/crear/";
    },
    postContrato: function() {
      return "/api/v1/contrato/crear/";
    },
    getContrato: function(code) {
      return "http://192.168.100.30:8003/api/v1/contrato/" + code ;
      //return "http://190.181.25.202:8000/api/v1/contrato/" + code ;
    },
    listencargado: function() {
      return "/api/v1/contrato/obtener/";
    },
    getEncargadoPoder: function(codigo_sucursal) {
      return "/api/v1/encargado-poder/"+codigo_sucursal+"/";
    },
    deleteContrato: function(pk) {
      return "/api/v1/contrato/delete/" + pk + "/";
    },
    editContrato: function(pk) {
      return "/api/v1/contratos/" + pk + "/";
    },

    // -------------- URLS RECLAMO -------------
    postReclamos: function() {
      return "/api/v1/reclamo/crear/";
    },
    // -------------- URLS PERSONA -------------
    crearListarPersona: function() {
      return "/api/v1/personas/";
    },
    deletePersona: function(pk) {
      return "/api/v1/personas/" + pk + "/";
    },
    editPersona: function(pk) {
      return "/api/v1/personas/" + pk + "/";
    },
    // -------------- URLS CONSULTAS -------------
    crearListarConsulta: function() {
      return "/api/v1/consultas/";
    },

    ListaPersona: function() {
      return "/api/v1/personas/list/";
    },
    DetalleConsulta: function(pk) {
      return "/api/v1/consultas/" + pk + "/";
    },

    // -------------- URLS ZONAS -------------
    crearListarZona: function () {
      return "/api/v1/zonas/"
    },

    deleteZona:function name(pk) {
      return "/api/v1/zona/" + pk 
    },

    editZona: function (pk) {
      return "/api/v1/zona/" + pk 
    },

     // -------------- URLS LOCALIDAD -------------
     crearListarLocalidad: function () {
      return "/api/v1/localidad"
    },

    // -------------- URLS GRUPO SOLIDARIO ----------------
    craarListarGrupoSolidario: function () {
      return "/api/v1/grupos/"
    },
    editGrupoSolidario: function (pk) {
      return "/api/v1/grupo/" + pk 
    },
    detailGrupoSolidario:function (pk) {
      return "/api/v1/grupo/" + pk
    },
    deleteGrupoSolidario:function (pk) {
      return "/api/v1/grupo/" + pk 
    },

    // -------------- URLS ARQUEOS ----------------
    crearListarArqueo: function () {
      return "/api/v1/arqueos/"
    },

    crearListarDiccionarioCorteMoneda: function () {
      return "/api/v1/corte"
    }
  }
};