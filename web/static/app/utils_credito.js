/**Typhead for domicilio solicitud */
var TypeaheadCiudad = function () {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var ciudad_comunidad_typehead = function (ciudades) {
		//console.log("cargando lista de ciudades")
		var substringMatcher = function (strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');

				$.each(strs, function (i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});

				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_ciudad').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad',
			source: substringMatcher(ciudades)
		});
		$('#kt_typeahead_ciudad').bind('typeahead:select', function (ev, suggestion) {
			if (app.solicitud2.zona_domicilio) 
				app.solicitud2.zona_domicilio=null;			
			app.solicitud2.ciudad = $('#kt_typeahead_ciudad').typeahead('val')
		});
	}

	return {
		init: function (ciudades) {				
			$('#kt_typeahead_ciudad').typeahead('destroy');
			ciudad_comunidad_typehead(ciudades);
		}
	};

}();

var TypeaheadZona = function () {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var zona_typehead = function (zonas) {
		//console.log("cargando lista de zonas")
		var substringMatcher = function (strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');

				$.each(strs, function (i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});

				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_zona').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad',
			source: substringMatcher(zonas)
		});
		$('#kt_typeahead_zona').bind('typeahead:select', function (ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			app.solicitud2.zona_domicilio = $('#kt_typeahead_zona').typeahead('val')
		});
	}

	return {
		init: function (zonas) {				
			$('#kt_typeahead_zona').typeahead('destroy');
			zona_typehead(zonas);
		}
	};

}();

/**Typhead for actividad economica >> direccion */
var TypeaheadCiudadActividad = function () {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var ciudad_comunidad_typehead = function (ciudades) {
		//console.log("cargando lista de ciudades")
		var substringMatcher = function (strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');

				$.each(strs, function (i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});

				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_ciudad_actividad').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad',
			source: substringMatcher(ciudades)
		});
		$('#kt_typeahead_ciudad_actividad').bind('typeahead:select', function (ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			if (app.direccion_actividad.zona) 
				app.direccion_actividad.zona=null;
			
			app.direccion_actividad.ciudad = $('#kt_typeahead_ciudad_actividad').typeahead('val')
		});
	}

	return {
		init: function (ciudades) {				
			$('#kt_typeahead_ciudad_actividad').typeahead('destroy');
			ciudad_comunidad_typehead(ciudades);
		}
	};

}();

var TypeaheadZonaActividad = function () {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var zona_typehead = function (zonas) {
		//console.log("cargando lista de zonas")
		var substringMatcher = function (strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');

				$.each(strs, function (i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});

				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_zona_actividad').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad',
			source: substringMatcher(zonas)
		});
		$('#kt_typeahead_zona_actividad').bind('typeahead:select', function (ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			app.direccion_actividad.zona = $('#kt_typeahead_zona_actividad').typeahead('val')
		});
	}

	return {
		init: function (zonas) {				
			$('#kt_typeahead_zona_actividad').typeahead('destroy');
			zona_typehead(zonas);
		}
	};

}();

var TypeaheadCiudadActividadSecundaria = function () {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var ciudad_comunidad_typehead = function (ciudades) {
		//console.log("cargando lista de ciudades")
		var substringMatcher = function (strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');

				$.each(strs, function (i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});

				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_ciudad_secundaria').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad',
			source: substringMatcher(ciudades)
		});
		$('#kt_typeahead_ciudad_secundaria').bind('typeahead:select', function (ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			app.direccion_actividad_secundaria.ciudad = $('#kt_typeahead_ciudad_secundaria').typeahead('val')
			if (app.direccion_actividad_secundaria.zona) 
				app.direccion_actividad_secundaria.zona=null;
			
		});
	}

	return {
		init: function (ciudades) {	
			//console.log("Iniciando ciudades secundaria");
			$('#kt_typeahead_ciudad_secundaria').typeahead('destroy');
			ciudad_comunidad_typehead(ciudades);
		}
	};

}();


var TypeaheadZonaActividadSecundaria = function () {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var zona_typehead = function (zonas) {
		//console.log("cargando lista de zonas")
		var substringMatcher = function (strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');

				$.each(strs, function (i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});

				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_zona_secundaria').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad',
			source: substringMatcher(zonas)
		});
		$('#kt_typeahead_zona_secundaria').bind('typeahead:select', function (ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			app.direccion_actividad_secundaria.zona = $('#kt_typeahead_zona_secundaria').typeahead('val')
		});
	}

	return {
		init: function (zonas) {	
			//console.log("Iniciando zonas secundaria");			
			$('#kt_typeahead_zona_secundaria').typeahead('destroy');
			zona_typehead(zonas);
		}
	};

}();

var avatar1 = new KTImageInput('kt_image_1');

$.fn.datepicker.dates['es'] = {
		days: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
		daysShort: ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"],
		daysMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
		months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Deciembre"],
		monthsShort: ["Ene", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
		today: "Hoy",
		clear: "Borrar",
		format: "yyyy-mm-dd",
		titleFormat: "MM yyyy", /* Leverages same syntax as 'format' */
		weekStart: 0
	};
// Class definition

var KTBootstrapTimepicker = function () {
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
	// Private functions
	var demos = function () {
		// minimum setup for actividad principal
		$('#kt_timepicker_inicial').timepicker({
			minuteStep: 15,
			defaultTime: '08:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad_economica.hora_inicio = $('#kt_timepicker_inicial').val();
		});
		$('#kt_timepicker_final').timepicker({
			minuteStep: 15,
			defaultTime: '18:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad_economica.hora_fin = $('#kt_timepicker_final').val();
		});
		// minimum setup
		$('#kt_datepicker_nacimiento').datepicker({
			rtl: KTUtil.isRTL(),
			todayHighlight: true,
			orientation: "bottom left",
			templates: arrows,
			language: 'es',
			daysShort: true,
			todayBtn: "linked",
			clearBtn: true,
		}).change(function (ev) {
			console.log(ev)
			//app.certificado.fecha_emision = $('#kt_datepicker_fecha_emision').val();
		});
	}

	return {
		// public functions
		init: function () {
			demos();
		}
	};
}();

var KTBootstrapTimepickerSecundario = function () {
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
	// Private functions
	var demos = function () {
		
		// minimum setup for actividad secundaria
		$('#kt_timepicker_inicial_secundario').timepicker({
			minuteStep: 15,
			defaultTime: '8:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad_secundaria.hora_inicio = $('#kt_timepicker_inicial_secundario').val();
		});
		$('#kt_timepicker_final_secundario').timepicker({
			minuteStep: 15,
			defaultTime: '18:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true

		}).change(function (ev) {
			//console.log(ev)
			app.actividad_secundaria.hora_fin = $('#kt_timepicker_final_secundario').val();
		});
	}

	return {
		// public functions
		init: function () {
			demos();
		}
	};
}();

// ************************** este codigo simbre debe ir al final ********************************


"use strict";
//var avatar1 = new KTImageInput('kt_image_1');
var KTFoto = function () {
	// Elements
	var avatar;
	var offcanvas;
	// Private functions
	var _initAside = function () {
		// Mobile offcanvas for mobile mode
		offcanvas = new KTOffcanvas('kt_profile_aside',{
            overlay: true,
            baseClass: 'offcanvas-mobile',
            //closeBy: 'kt_user_profile_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}
	var _initForm = function() {
		avatar = new KTImageInput('kt_image_foto');
	}
	return {
		// public functions
		init: function() {
			_initAside();
			_initForm();
		}
	};
}();
var KTFotocopia = function () {
	// Elements
	var avatar;
	var offcanvas;
	// Private functions
	var _initAside = function () {
		// Mobile offcanvas for mobile mode
		offcanvas = new KTOffcanvas('kt_profile_aside',{
            overlay: true,
            baseClass: 'offcanvas-mobile',
            //closeBy: 'kt_user_profile_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}
	var _initForm = function() {
		avatar = new KTImageInput('kt_image_fotocopia');
	}
	return {
		// public functions
		init: function() {
			_initAside();
			_initForm();
		}
	};
}();
var KTCIAnverso = function () {
	// Elements
	var avatar;
	var offcanvas;
	// Private functions
	var _initAside = function () {
		// Mobile offcanvas for mobile mode
		offcanvas = new KTOffcanvas('kt_profile_aside',{
            overlay: true,
            baseClass: 'offcanvas-mobile',
            //closeBy: 'kt_user_profile_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}
	var _initForm = function() {
		avatar = new KTImageInput('kt_image_foto_ci1');
	}
	return {
		// public functions
		init: function() {
			_initAside();
			_initForm();
		}
	};
}();
var KTCIReverso = function () {
	// Elements
	var avatar;
	var offcanvas;
	// Private functions
	var _initAside = function () {
		// Mobile offcanvas for mobile mode
		offcanvas = new KTOffcanvas('kt_profile_aside',{
            overlay: true,
            baseClass: 'offcanvas-mobile',
            //closeBy: 'kt_user_profile_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}
	var _initForm = function() {
		avatar = new KTImageInput('kt_image_foto_ci2');
	}
	return {
		// public functions
		init: function() {
			_initAside();
			_initForm();
		}
	};
}();
var KTAgua = function () {
	// Elements
	var avatar;
	var offcanvas;
	// Private functions
	var _initAside = function () {
		// Mobile offcanvas for mobile mode
		offcanvas = new KTOffcanvas('kt_profile_aside',{
            overlay: true,
            baseClass: 'offcanvas-mobile',
            //closeBy: 'kt_user_profile_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}
	var _initForm = function() {
		avatar = new KTImageInput('kt_image_factura_agua');
	}
	return {
		// public functions
		init: function() {
			_initAside();
			_initForm();
		}
	};
}();
var KTLuz = function () {
	// Elements
	var avatar;
	var offcanvas;
	// Private functions
	var _initAside = function () {
		// Mobile offcanvas for mobile mode
		offcanvas = new KTOffcanvas('kt_profile_aside',{
            overlay: true,
            baseClass: 'offcanvas-mobile',
            //closeBy: 'kt_user_profile_aside_close',
            toggleBy: 'kt_subheader_mobile_toggle'
        });
	}
	var _initForm = function() {
		avatar = new KTImageInput('kt_image_factura_luz');
	}
	return {
		// public functions
		init: function() {
			_initAside();
			_initForm();
		}
	};
}();

jQuery(document).ready(function() {
	KTFoto.init();
	KTFotocopia.init();
	KTCIAnverso.init();
	KTCIReverso.init();
	KTLuz.init();
	KTAgua.init();
});
