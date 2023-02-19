
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

var DatepickerAdquisicion = function () {
	/**
	* Datepicker for new activo  fijo
	* 
	*/
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
	var calendar_ini = function() {
		// enable clear button
		$('#kt_datepicker_adquisicion').datepicker({
			rtl: KTUtil.isRTL(),
			todayHighlight: true,
			clearBtn: true,
			autoclose: true,
			format: 'yyyy-mm-dd',
			templates: arrows,
			orientation: 'bottom',
			language: 'es',
		}).change(function(ev) {
			app.activo_fijo.fecha_adquisicion= $('#kt_datepicker_adquisicion').val();
		});
	}
	
	return {
		init: function () {
			calendar_ini();
		}
	};
}();

var DatepickerAdquisicionIni = function () {
	/**
	* Date picker for filter activo fijo
	*/
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
	var calendar_ini = function() {
		// enable clear button
		$('#kt_datepicker_ini').datepicker({
			rtl: KTUtil.isRTL(),
			clearBtn: true,
			autoclose: true,
			format: 'yyyy-mm-dd',
			templates: arrows,
			orientation: 'bottom',
			language: 'es',
		}).change(function(ev) {
			app.filtrar_activo.fecha_adquisicion_ini= $('#kt_datepicker_ini').val();
		});
	}
	
	return {
		init: function () {
			calendar_ini();
		}
	};
}();

var DatepickerAdquisicionFin = function() {
	/**
	* Date picker for filter activo fijo
	*/
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
	var calendar_fin = function() {
		// enable clear button
		$('#kt_datepicker_fin').datepicker({
			rtl: KTUtil.isRTL(),
			clearBtn: true,
			autoclose: true,
			format: 'yyyy-mm-dd',
			templates: arrows,
			orientation: 'bottom',
			language: 'es',
		}).change(function(ev) {
			app.filtrar_activo.fecha_adquisicion_fin= $('#kt_datepicker_fin').val();
		});
	}
	
	return {
		init: function () {
			calendar_fin();
		}
	};
}();


const la_paz = {
	lat: -16.503796017651304,
	lng: -68.16268515902941,
};
let marker_domicilio;
function initMapDomicilio() {
	// Map for Domicilio in form new client
	const map = new google.maps.Map(document.getElementById("gmap_1"), {
		zoom: 15,
		center: la_paz,
	});
	
	const marker_domicilio = new google.maps.Marker({
		position: la_paz,
		map: map,
		draggable: true,
		title: "Arrastra el marcador",
	});
	google.maps.event.addListener(marker_domicilio, 'dragend', function(event) {
		//console.log(this.getPosition().lat());
		//console.log(this.getPosition().lng());
		app.domicilio.punto_gps = this.getPosition().lat() + "," + this.getPosition().lng();
	});
}

let marker;
function initMapActividad() {
	// Map for Actividad principal in form new client
	const map = new google.maps.Map(document.getElementById("gmap_2"), {
		zoom: 15,
		center: la_paz,
	});
	
	const marker = new google.maps.Marker({
		position: la_paz,
		map: map,
		draggable: true,
		title: "Arrastra el marcador",
	});
	google.maps.event.addListener(marker, 'dragend', function(event) {
		//console.log(this.getPosition().lat());
		//console.log(this.getPosition().lng());
		app.direccion_actividad.punto_gps = this.getPosition().lat() + ", " + this.getPosition().lng();
		
	});
}

let markerSecundaria;
function initMapActividadSecundaria() {
	// Map for Actividad secundaria in form new client
	const map = new google.maps.Map(document.getElementById("gmap_3"), {
		zoom: 15,
		center: la_paz,
	});
	
	const markerSecundaria = new google.maps.Marker({
		position: la_paz,
		map: map,
		draggable: true,
		title: "Arrastra el marcador",
	});
	google.maps.event.addListener(markerSecundaria, 'dragend', function(event) {
		//console.log(this.getPosition().lat());
		//console.log(this.getPosition().lng());
		app.direccion_actividad_2.punto_gps = this.getPosition().lat() + ", " + this.getPosition().lng();
		
	});
}

let markerConyuge;
function initMapConyuge() {
	// Map for Direccion Conyuge in form new client
	const map = new google.maps.Map(document.getElementById("gmap_4"), {
		zoom: 15,
		center: la_paz,
	});
	
	const markerConyuge = new google.maps.Marker({
		position: la_paz,
		map: map,
		draggable: true,
		title: "Arrastra el marcador",
	});
	google.maps.event.addListener(markerConyuge, 'dragend', function(event) {
		//console.log(this.getPosition().lat());
		//console.log(this.getPosition().lng());
		app.conyuge_trabajo.punto_gps = this.getPosition().lat() + ", " + this.getPosition().lng();
		
	});
}




var DomicilioTypeahead = function() {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var ciudad_comunidad_domicilio_typehead = function(ciudades) {
		console.log("cargando lista de actividades")
		var substringMatcher = function(strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');
				
				$.each(strs, function(i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});
				
				cb(matches);
			};
		};
		//console.log("--------------------", LEVEL)
		if (LEVEL == "L3") {
			$('#kt_typeahead_domicilio').typeahead({
				hint: true,
				highlight: true,
				minLength: 1
			}, {
				name: 'ciudad_comunidad',
				source: substringMatcher(ciudades)
			});
			$('#kt_typeahead_domicilio').bind('typeahead:select', function(ev, suggestion) {
				//console.log('Selection: ' + suggestion);
				app.clienteL3.datos_adicionales.domicilio.ubicacion_base.ciudad_comunidad = $('#kt_typeahead_domicilio').typeahead('val')
			});
		}
	}
	
	return {
		init: function(ciudades) {
			$('#kt_typeahead_domicilio').typeahead('destroy');
			ciudad_comunidad_domicilio_typehead(ciudades);
		}
	};
}();

var UbicacionActividadReferenciaTypeahead = function() {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var ciudad_comunidad_typehead = function(ciudades) {
		//console.log("cargando lista de ciudades para actividades")
		var substringMatcher = function(strs) {
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');
				
				$.each(strs, function(i, str) {
					if (substrRegex.test(str)) {
						matches.push(str);
					}
				});
				
				cb(matches);
			};
		};
		
		var SET_TYPEHEAD = {
			hint: true,
			highlight: true,
			minLength: 1
		};
		//console.log("--------------------", LEVEL)
		$('#kt_typeahead_ubicacion_actividad_economica, #kt_typeahead_ubicacion_referencia, #kt_typeahead_conyuge, #kt_typeahead_edit').typeahead({
			hint: true,
			highlight: true,
			minLength: 1
		}, {
			name: 'ciudad_comunidad',
			source: substringMatcher(ciudades)
		});
		$('#kt_typeahead_ubicacion_actividad_economica, #kt_typeahead_ubicacion_referencia, #kt_typeahead_conyuge, #kt_typeahead_edit ').bind('typeahead:select', function(ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			app.actividad_economica.ubicacion.ciudad_comunidad = $('#kt_typeahead_ubicacion_actividad_economica').typeahead('val')
			app.referencia_personal.radicatoria.ciudad_comunidad = $('#kt_typeahead_ubicacion_referencia').typeahead('val')
			app.conyuge.lugar_nacimiento.ciudad_comunidad = $('#kt_typeahead_conyuge').typeahead('val')
			app.cliente_edit.lugar_nacimiento.ciudad_comunidad = $('#kt_typeahead_edit').typeahead('val')
		});
		
		// >>  Para edicion de cliente DOMICILIO
		$('#kt_typeahead_edit_domicilio').typeahead(SET_TYPEHEAD, {
			name: 'ciudad_comunidad',
			source: substringMatcher(ciudades)
		});
		$('#kt_typeahead_edit_domicilio').bind('typeahead:select', function(ev, suggestion) {
			//console.log('Selection: ' + suggestion);
			app.cliente_edit.datos_adicionales.domicilio.ciudad_comunidad = $('#kt_typeahead_edit_domicilio').typeahead('val')
		});
	}
	
	return {
		init: function(ciudades) {
			$('#kt_typeahead_ubicacion_actividad_economica, #kt_typeahead_ubicacion_referencia, #kt_typeahead_conyuge').typeahead('destroy');
			$('#kt_typeahead_edit, kt_typeahead_edit_domicilio').typeahead('destroy');
			//console.log("------------------------> ", ciudades)
			ciudad_comunidad_typehead(ciudades);
		}
	};
}();

var KTTagifyDias = function() {
	//DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sabado", "domingo"];
	// Private functions
	
	var tags = function() {
		var input = document.getElementById('kt_tagify_dias');
		var tagify = new Tagify(input, {
			pattern: /^.{0,20}$/, // Validate typed tag(s) by Regex. Here maximum chars length is defined as "20"
			delimiters: ", ", // add new tags when a comma or a space character is entered
			maxTags: 7,
			blacklist: ["fuck", "shit", "pussy"],
			keepInvalidTags: true, // do not remove invalid tags (but keep them marked as invalid)
			//whitelist:DIAS,
			transformTag: transformTag,
			dropdown: {
				enabled: 1,
			}
		});
		
		function transformTag(tagData) {
			
			//tagData.class = 'tagify__tag tagify__tag-light--' + states[KTUtil.getRandomInt(0, 8)];
			dia = tagData.value.toLowerCase();
			if (dia == 'lunes' || dia == 'martes' || dia == 'miercoles' || dia == 'jueves' || dia == 'viernes') {
				tagData.class = 'tagify__tag tagify__tag-light--success';
			}
			if (dia == 'sabado' || dia == 'domingo') {
				tagData.class = 'tagify__tag tagify__tag-light--info';
			}
		}
		
		tagify.on('add', function(e) {
			console.log(e.detail)
		});
		
		tagify.on('invalid', function(e) {
			console.log(e, e.detail);
		});
	}
	return {
		// public functions
		
		init: function() {
			//console.log("INIT Tagify")
			tags();
		}
	};
}();

var TimepickerActividadEconomica = function () {
	
	// Private functions
	var demos = function () {
		// minimum setup
		$('#kt_timepicker_inicio').timepicker({
			defaultTime: '08:00',
			minuteStep: 15,
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function(ev) {
			app.actividad_economica.hora_inicio = $('#kt_timepicker_inicio').val();
		});
		
		$('#kt_timepicker_fin').timepicker({
			defaultTime: '18:00',
			minuteStep: 15,
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function(ev) {
			app.actividad_economica.hora_fin = $('#kt_timepicker_fin').val();
		});
	}
	
	return {
		// public functions
		init: function() {
			demos();
		}
	};
}();

var ActividadTypeahead = function(actividad) {
	//https://github.com/twitter/typeahead.js/blob/master/doc/jquery_typeahead.md
	var actividad_typehead = function(actividad) {
		//console.log("cargando lista de actividades para actividades");
		
		var substringMatcher = function(strs) {
			//console.log("-----.->", strs);
			
			return function findMatches(q, cb) {
				var matches, substringRegex;
				matches = [];
				substrRegex = new RegExp(q, 'i');
				
				$.each(strs, function(i, str) {
					//console.log(str.nombre)
					if (substrRegex.test(str.nombre)) {
						matches.push(str.nombre);
					}
				});
				
				cb(matches);
			};
		};
		
		$('#kt_typeahead_actividad').typeahead({
			hint: true,
			highlight: true,
			minLength: 3
		}, {
			name: 'actividades',
			source: substringMatcher(actividad)
		});
		$('#kt_typeahead_actividad').bind('typeahead:select', function(ev, suggestion) {
			console.log('Selection: ' + suggestion);
			app.actividad_economica.actividad = $('#kt_typeahead_actividad').typeahead('val')
		});
	}
	/*
	
	*/
	
	return {
		init: function(actividad) {
			$('#kt_typeahead_actividad').typeahead('destroy');
			//console.log("-----------------.->", actividad);
			
			actividad_typehead(actividad);
		}
	};
}();

let marker_edit;
function initMapEdit(position) {
	console.log("cargando punto en mapa: ",position)
	var point;
	if(position!=null){
		position = position.replace(/\s/g, '')
		const lat = parseFloat(position.split(',')[0]); 
		const lng = parseFloat(position.split(',')[1]); 
		point = {
			lat: lat,
			lng: lng,
		};
		//console.log("-----------------------> ", point)
	}else{
		point = {
			lat: -16.503796017651304,
			lng: -68.16268515902941,
		};
	}
	
	const mapEdit = new google.maps.Map(document.getElementById("gmap_edit"), {
		zoom: 15,
		center: point,
	});
	
	const marker_edit = new google.maps.Marker({
		position: point,
		map: mapEdit,
		draggable: true,
		title: "Arrastra el marcador",
	});
	
	google.maps.event.addListener(marker_edit, 'dragend', function(event) {
		//console.log(this.getPosition().lat());
		//console.log(this.getPosition().lng());
		//app.position = this.getPosition().lat() + ", " + this.getPosition().lng();
		app.cliente_edit.datos_adicionales.domicilio.ubicacion_gps = this.getPosition().lat() + "," + this.getPosition().lng();
		
	});
}

var TEMPLATE = {
	leftArrow: '<i class="la la-angle-left"></i>',
	rightArrow: '<i class="la la-angle-right"></i>'
}

var DatePickerIni = function () {
	return {
		init: function () {		
			$("#kt_datepicker_ini").datepicker({
				todayHighlight: true,
				format: 'yyyy-mm-dd',
				language: 'es',
				orientation: "bottom left",
				templates: TEMPLATE,
			}).on("changeDate", function (event) {
				//console.log(event)
				app.filter_activo.fecha_adquisicion_ini = $('#kt_datepicker_ini').val();
			})
		}
	}
};

var DatePickerFin = function () {
	return {
		init: function () {			
			$("#kt_datepicker_fin").datepicker({
				todayHighlight: true,
				format: 'yyyy-mm-dd',
				language: 'es',
				orientation: "bottom left",
				templates: TEMPLATE,
			}).on("changeDate", function (event) {
				//console.log(event)
				app.filter_activo.fecha_adquisicion_fin = $('#kt_datepicker_fin').val();
			})
		}
	}
};


var actividadTimepicker = function () {	
	// Private functions
	var horarioActividadInicio = function () {
		// minimum setup for actividad principal
		$('#actividad_hora_inicial').timepicker({
			minuteStep: 15,
			defaultTime: '08:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad.hora_inicio = $('#actividad_hora_inicial').val();
		});
	}
	var horarioActividadFin = function () {
		// minimum setup for actividad principal
		$('#actividad_hora_final').timepicker({
			minuteStep: 15,
			defaultTime: '18:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad.hora_fin = $('#actividad_hora_final').val();
		});
	}

	return {
		// public functions
		init: function () {
			horarioActividadInicio();
			horarioActividadFin();
		}
	};
}();

var actividad2Timepicker = function () {	
	// Private functions
	var horarioActividadInicio = function () {
		// minimum setup for actividad principal
		$('#actividad_2_hora_inicial').timepicker({
			minuteStep: 15,
			defaultTime: '08:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad_2.hora_inicio = $('#actividad_2_hora_inicial').val();
		});
	}
	var horarioActividadFin = function () {
		// minimum setup for actividad principal
		$('#actividad_2_hora_final').timepicker({
			minuteStep: 15,
			defaultTime: '18:00',
			showSeconds: false,
			showMeridian: false,
			snapToStep: true
		}).change(function (ev) {
			//console.log(ev)
			app.actividad_2.hora_fin = $('#actividad_2_hora_final').val();
		});
	}

	return {
		// public functions
		init: function () {
			horarioActividadInicio();
			horarioActividadFin();
		}
	};
}();
//jQuery(document).ready(function () {
//AdvancedSearchActivos.init()
//});


/** ***************** validation functions ************************ */
function validateTelefono(telefono) {
	// Funtion for validate phone number
	var re = /^[6-7]{1}[0-9]{7}$|^[2]{1}[0-9]{7}$/;
	return re.test(telefono);
};
function validateCapitalLetterString(string) {
	var re = /^[A-Z\s]{1}[a-z]*$/;
	return re.test(string);
	//funcion para cambiar a mayuscula
}
function validateEmail(string) {
	var re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
	return re.test(string);
}




/*

var DatepickerNacimiento = function () {
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
	var calendarNacimiento = function() {
		// enable clear button
		$('#kt_datepicker_nacimiento').datepicker({
			rtl: KTUtil.isRTL(),
			clearBtn: true,
			autoclose: true,
			format: 'yyyy-mm-dd',
			daysShort: true,
			//formatSubmit: 'yyyy-mm-dd',
			templates: arrows,
			language: 'es',
		}).change(function(ev) {
			app.clienteL2.fecha_nacimiento = $('#kt_datepicker_nacimiento').val();
			app.clienteL3.fecha_nacimiento = $('#kt_datepicker_nacimiento').val();
		});
		
	}
	
	return {
		// public functions
		init: function() { calendarNacimiento(); }
	};
}();

var DatepickerVigencia = function() {
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
	var calendarVigencia = function() {
		// enable clear button
		$('#kt_datepicker_vigencia, #kt_datepicker_3_validate').datepicker({
			rtl: KTUtil.isRTL(),
			clearBtn: true,
			autoclose: true,
			format: 'yyyy-mm-dd',
			templates: arrows,
			language: 'es',
		}).change(function(ev) {
			app.clienteL2.vigencia_documento_identidad = $('#kt_datepicker_vigencia').val();
			app.clienteL3.vigencia_documento_identidad = $('#kt_datepicker_vigencia').val();
		});
		
	}
	
	return {
		init: function() { calendarVigencia(); }
	};
}();

var DatepickerConyuge = function() {
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
	var calendarConyuge = function() {
		// enable clear button
		$('#kt_datepicker_nacimiento_conyuge').datepicker({
			rtl: KTUtil.isRTL(),
			clearBtn: true,
			autoclose: true,
			format: 'yyyy-mm-dd',
			templates: arrows,
			language: 'es',
		}).change(function(ev) {
			app.conyuge.fecha_nacimiento= $('#kt_datepicker_nacimiento_conyuge').val();
		});
		
	}
	
	return {
		init: function() { calendarConyuge(); }
	};
}();

*/