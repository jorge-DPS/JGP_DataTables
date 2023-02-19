
  function NumerosaLetras(cantidad) {
    var decPart = cantidad.toString().split(",")[1];

    var numero = 0;
    cantidad = parseFloat(cantidad);

    if (cantidad == "0.00" || cantidad == "0") {
      return "CERO con 00/100 ";
    } else {
      var ent = cantidad.toString().split(".");


      var arreglo = separar_split(ent[0]);
      var longitud = arreglo.length;

      switch (longitud) {
        case 1:
          numero = unidades(arreglo[0]);
          break;
        case 2:
          numero = decenas(arreglo[0], arreglo[1]);
          break;
        case 3:
          numero = centenas(arreglo[0], arreglo[1], arreglo[2]);
          break;
        case 4:
          numero = unidadesdemillar(arreglo[0], arreglo[1], arreglo[2], arreglo[3]);
          break;
        case 5:
          numero = decenasdemillar(arreglo[0], arreglo[1], arreglo[2], arreglo[3], arreglo[4]);
          break;
        case 6:
          numero = centenasdemillar(arreglo[0], arreglo[1], arreglo[2], arreglo[3], arreglo[4], arreglo[5]);
          break;
      }
      return numero + "  " + decPart + "/100";
    }
  };

  function unidades(unidad) {
    var unidades = Array('UN ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ', 'OCHO ', 'NUEVE ');


    return unidades[unidad - 1];
  };

  function decenas(decena, unidad) {
    var diez = Array('ONCE ', 'DOCE ', 'TRECE ', 'CATORCE ', 'QUINCE', 'DIECISEIS ', 'DIECISIETE ', 'DIECIOCHO ', 'DIECINUEVE ');
    var decenas = Array('DIEZ ', 'VEINTE ', 'TREINTA ', 'CUARENTA ', 'CINCUENTA ', 'SESENTA ', 'SETENTA ', 'OCHENTA ', 'NOVENTA ');

    if (decena == 0 && unidad == 0) {
      return "";
    }

    if (decena == 0 && unidad > 0) {
      return unidades(unidad);
    }

    if (decena == 1) {
      if (unidad == 0) {
        return decenas[decena - 1];
      } else {
        return diez[unidad - 1];
      }
    } else if (decena == 2) {
      if (unidad == 0) {
        return decenas[decena - 1];
      }
      else if (unidad == 1) {
        return veinte = "VEINTI" + "UNO";
      }
      else {
        return veinte = "VEINTI" + unidades(unidad);
      }
    } else {

      if (unidad == 0) {
        return decenas[decena - 1] + " ";
      }
      if (unidad == 1) {
        return decenas[decena - 1] + " Y " + "UNO";
      }

      return decenas[decena - 1] + " Y " + unidades(unidad);
    }
  };

  function centenas(centena, decena, unidad) {
    var centenas = Array("CIENTO ", "DOSCIENTOS ", "TRESCIENTOS ", "CUATROCIENTOS ", "QUINIENTOS ", "SEISCIENTOS ", "SETECIENTOS ", "OCHOCIENTOS ", "NOVECIENTOS ");

    if (centena == 0 && decena == 0 && unidad == 0) {
      return "";
    }
    if (centena == 1 && decena == 0 && unidad == 0) {
      return "CIEN ";
    }

    if (centena == 0 && decena == 0 && unidad > 0) {
      return unidades(unidad);
    }

    if (decena == 0 && unidad == 0) {
      return centenas[centena - 1] + "";
    }

    if (decena == 0) {
      var numero = centenas[centena - 1] + "" + decenas(decena, unidad);
      return numero.replace(" Y ", " ");
    }
    if (centena == 0) {

      return decenas(decena, unidad);
    }

    return centenas[centena - 1] + "" + decenas(decena, unidad);

  };

  function unidadesdemillar(unimill, centena, decena, unidad) {
    var numero = unidades(unimill) + " MIL " + centenas(centena, decena, unidad);
    numero = numero.replace("UN  MIL ", "MIL ");
    if (unidad == 0) {
      return numero.replace(" Y ", " ");
    } else {
      return numero;
    }
  };

  function decenasdemillar(decemill, unimill, centena, decena, unidad) {
    var numero = decenas(decemill, unimill) + " MIL " + centenas(centena, decena, unidad);
    return numero;
  };

  function centenasdemillar(centenamill, decemill, unimill, centena, decena, unidad) {

    var numero = 0;
    numero = centenas(centenamill, decemill, unimill) + " MIL " + centenas(centena, decena, unidad);

    return numero;
  };

  function separar_split(texto) {
    var contenido = new Array();
    for (var i = 0; i < texto.length; i++) {
      contenido[i] = texto.substr(i, 1);
    }
    return contenido;
  };

  function NumLetras(cantidad) {
    var decPart = cantidad.toString().split(",")[1];

    var numero = 0;
    cantidad = parseFloat(cantidad);

    if (cantidad == "0.00" || cantidad == "0") {
      return numero;
    } else {
      var ent = cantidad.toString().split(".");


      var arreglo = separar_split(ent[0]);
      var longitud = arreglo.length;

      switch (longitud) {
        case 1:
          numero = unidades(arreglo[0]);
          break;
        case 2:
          numero = decenas(arreglo[0], arreglo[1]);
          break;
        case 3:
          numero = centenas(arreglo[0], arreglo[1], arreglo[2]);
          break;
        case 4:
          numero = unidadesdemillar(arreglo[0], arreglo[1], arreglo[2], arreglo[3]);
          break;
        case 5:
          numero = decenasdemillar(arreglo[0], arreglo[1], arreglo[2], arreglo[3], arreglo[4]);
          break;
        case 6:
          numero = centenasdemillar(arreglo[0], arreglo[1], arreglo[2], arreglo[3], arreglo[4], arreglo[5]);
          break;
      }
      return numero ;
    }
  };

  function Porcentaje(cantidad) {
    var decPart = cantidad.toString().split(",")[1];

    var numero = 0;
    cantidad = parseFloat(cantidad);

    if (cantidad == "0.00" || cantidad == "0") {
      return "CERO PUNTO "+ unidades2(decPart/10);
    } else {
      var ent = cantidad.toString().split(".");


      var arreglo = separar_split(ent[0]);
      var longitud = arreglo.length;

      switch (longitud) {
        case 1:
          numero = unidades2(arreglo[0]);
          break;
      }
      if (decPart == '00'){
        return numero + " PUNTO " + "CERO";
      }else{
        return numero + " PUNTO " + unidades2(decPart/10);  
      }
    }
  };

  function unidades2(unidad) {
    var unidades = Array('UNO ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ', 'OCHO ', 'NUEVE ');


    return unidades[unidad - 1];
  };



/*
  $.fn.datepicker.dates['es'] = {
    days: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
    daysShort: ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"],
    daysMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
    months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Deciembre"],
    monthsShort: ["Ene", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
    today: "Hoy",
    clear: "Borrar",
    format: "yyyy-mm-dd",
    titleFormat: "MM yyyy",
    weekStart: 0
  };
  var arrows;
  if (KTUtil.isRTL()) {
    arrows = {
      leftArrow: '<i class="la la-angle-right"></i>',
      rightArrow: '<i class="la la-angle-left"></i>'
    }
  } else {
    arrows = {
      leftArrow: '<i class="la la-angle-left"></i>',
      rightArrow: '<i class="la la-angle-right"></i>'
    }
  }
  
  var DatepickerCertificado = function() {
    //console.log("iniciando calendario de certificado")
    // Private functions
    var calendarCertificado = function() {
      // enable clear button

      var date = $('#kt_datepicker_fecha_emision').datepicker({
        rtl: KTUtil.isRTL(),
        clearBtn: true,
        autoclose: true,
        format: 'yyyy-mm-dd',
        daysShort: true,
        todayHighlight: true,
        todayBtn: "linked",
        clearBtn: true,
        //formatSubmit: 'yyyy-mm-dd',
        templates: arrows,
        language: 'es',
      }).change(function(ev) {
        app.certificado.fecha_emision = $('#kt_datepicker_fecha_emision').val();
      });

    }

    return {
      // public functions
      init: function() {
        calendarCertificado();
      }
    };
  }();
  var DatepickerCertificadoEdit = function() {
    //console.log("iniciando calendario de certificado")    

    // Private functions
    var calendarCertificado = function() {
      // enable clear button

      var date = $('#kt_datepicker_fecha_vencimiento').datepicker({
        rtl: KTUtil.isRTL(),
        clearBtn: true,
        autoclose: true,
        format: 'yyyy-mm-dd',
        daysShort: true,
        todayHighlight: true,
        todayBtn: "linked",
        clearBtn: true,
        //formatSubmit: 'yyyy-mm-dd',
        templates: arrows,
        language: 'es',
      }).change(function(ev) {
        app.certificado.fecha_vencimiento = $('#kt_datepicker_fecha_vencimiento').val();
      });

    }

    return {
      // public functions
      init: function() {
        calendarCertificado();
      }
    };
  }();
  */