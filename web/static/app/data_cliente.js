/**
 * In this file include the datas of the cliente.js
 */
var csrf_token = { headers: { "X-CSRFToken": csrftoken } };
var CLIENTE_DATA = {
	primer_nombre: 'Freddy',
	segundo_nombre: 'Marcos',
	tercer_nombre: null,
	apellido_paterno: 'Vega',
	apellido_materno: 'Mendez',
	apellido_esposo: null,
	telefono_1: '76543210',
	numero_documento: '654125630',
	complemento_documento: null,
	extension_documento: 'OR',
	apodo: null,
	genero: 'F',
	fecha_nacimiento: null,
	lugar_nacimiento: null,
	nacionalidad: 'BO',
	estado_civil: 'S',
	estado_civil_verificado: 'C',
	observaciones: 'Esta persona es una persona muy buena y confiable',
	numero_dependientes: 1,
	telefono_2: null,
	correo_electronico: 'correo_cliente@gmail.com',
	estado: 'V',
};
var CLIENTE = {
	primer_nombre: null,
	segundo_nombre: null,
	tercer_nombre: null,
	apellido_paterno: null,
	apellido_materno: null,
	apellido_esposo: null,
	telefono_1: null,
	numero_documento: null,
	complemento_documento: null,
	extension_documento: null,
	apodo: null,
	genero: null,
	fecha_nacimiento: null,
	lugar_nacimiento: null,
	nacionalidad: 'BO',
	estado_civil: null,
	estado_civil_verificado: 'C',
	observaciones: null,
	numero_dependientes: 0,
	telefono_2: null,
	correo_electronico: null,
	estado: null,
};
var CONYUGE_DATA = {
	primer_nombre: 'Rosario',
	segundo_nombre: 'Lorena',
	tercer_nombre: '',
	apellido_paterno: 'Gonzales',
	apellido_materno: 'Garcia',
	apellido_esposo: '',
	telefono_1: '65412301',
	numero_documento: '5412541',
	complemento_documento: '',
	extension_documento: 'SC',
	ocupacion: 'Ama de casa',
	//ubicacion_trabajo: UBICACION_TRABAJO_CONYUGE_DATA,
};
var CONYUGE = {
	primer_nombre: null,
	segundo_nombre: null,
	tercer_nombre: null,
	apellido_paterno: null,
	apellido_materno: null,
	apellido_esposo: null,
	telefono_1: null,
	numero_documento: null,
	complemento_documento: null,
	extension_documento: null,
	ocupacion: null,
	//ubicacion_trabajo: null,
};
var UBICACION_TRABAJO_CONYUGE_DATA = {
	ubicacion: {
		departamento: 'La Paz',
		provincia: 'Murillo',
		ciudad_comunidad: 'La Paz',
		zona_urbanizacion: 'San Pedro',
	},
	calle_avenida: 'Perez Velasco',
	nombre_numero: '25',
	referencia: 'Frente a plaza Abaroa',
	tipo_tenencia: 'P',
	anios_residencia: 5,
	punto_gps: null,
};
var UBICACION_TRABAJO_CONYUGE = {
	ubicacion: {
		departamento: '200',
		provincia: null,
		ciudad_comunidad: null,
		zona_urbanizacion: null,
	},
	calle_avenida: null,
	nombre_numero: null,
	referencia: null,
	tipo_tenencia: null,
	anios_residencia: null,
	punto_gps: null,
};
var REFERENCIA_DATA = {
	nombre_apellido: 'Juan Perez',
	telefono: '65412363',
	parentesco: 'P',
	tipo_referencia: 'F',
	direccion: 'El Alto, z. Bolivar "D", calle 134, Nro. 23',
};
var REFERENCIA = {
	nombre_apellido: null,
	telefono: null,
	parentesco: null,
	direccion: null,
	tipo_referencia: 'P',
};
var DOMICILIO = {
	ubicacion: {
		departamento: '200',
		provincia: null,
		ciudad_comunidad: null,
		zona_urbanizacion: null,
	},
	calle_avenida: null,
	nombre_numero: null,
	referencia: null,
	tipo_tenencia: null,
	anios_residencia: null,
	punto_gps: null,
};
var DOMICILIO_DATA = {
	ubicacion: {
		departamento: 'La Paz',
		provincia: 'Murillo',
		ciudad_comunidad: 'La Paz',
		zona_urbanizacion: 'San Pedro',
	},
	calle_avenida: 'Perez Velasco',
	nombre_numero: '25',
	referencia: 'Frente a plaza Abaroa',
	tipo_tenencia: 'P',
	anios_residencia: 5,
	punto_gps: null,
};
var ACTIVIDAD_DATA = {
	documento: null,
	descripcion: 'Trabajo de medio tiempo de venta de material de construcción',
	anios_experiencia: 5,
	anios_negocio: 4,
	caedec: null,
	dias_laborales: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
	hora_inicio: '08:30',
	hora_fin: '18:00',
	tipo_tenencia: 'P',
	tipo_actividad: 'F',
	tipo_ingreso: 'I',
	cliente: null,
	es_principal: false,
	telefono: '23454514',
	direccion: DIRECCION_ACTIVIDAD_DATA,
};
var ACTIVIDAD = {
	documento: null,
	descripcion: null,
	anios_experiencia: 0,
	anios_negocio: 0,
	caedec: null,
	dias_laborales: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
	hora_inicio: '8:00',
	hora_fin: '18:00',
	tipo_tenencia: null,
	tipo_actividad: 'F',
	tipo_ingreso: 'I',
	cliente: null,
	es_principal: null,
	telefono: null,
	direccion: DIRECCION_ACTIVIDAD,
};
var DIRECCION_ACTIVIDAD_DATA = {
	ubicacion: {
		departamento: 'La Paz',
		provincia: 'Murillo',
		ciudad_comunidad: 'La Paz',
		zona_urbanizacion: 'San Pedro',
	},
	calle_avenida: 'Perez Velasco',
	nombre_numero: '25',
	referencia: 'Frente a plaza Abaroa',
	tipo_tenencia: null, // este campo no se usa en actividad economica
	anios_residencia: 5,
	punto_gps: null,
};
var DIRECCION_ACTIVIDAD = {
	ubicacion: {
		departamento: '200',
		provincia: null,
		ciudad_comunidad: null,
		zona_urbanizacion: null,
	},
	calle_avenida: null,
	nombre_numero: null,
	referencia: null,
	tipo_tenencia: null,
	anios_residencia: null,
	punto_gps: null,
};
var UBICACION = {
	departamento: '200',
	provincia: null,
	ciudad_comunidad: null,
	zona_urbanizacion: null,
};

var ERROR_CLIENTE_L1 = {
	primer_nombre: [],
	segundo_nombre: null,
	tercer_nombre: null,
	apellido_paterno: [],
	apellido_materno: null,
	numero_documento_identidad: [],
	complemento_documento_identidad: null,
	extension_documento_identidad: null,
};

/** Dict for fecha_nacimiento */
var MESES = {
	'1': 'Enero',
	'2': 'Febrero',
	'3': 'Marzo',
	'4': 'Abril',
	'5': 'Mayo',
	'6': 'Junio',
	'7': 'Julio',
	'8': 'Agosto',
	'9': 'Septiembre',
	'10': 'Octubre',
	'11': 'Noviembre',
	'12': 'Diciembre',
}

/** Dict for departamentos */
var DEPARTAMENTOS = {
	'200': 'La Paz',
  '100': 'Chuquisaca',
  '300': 'Cochabamba',
  '400': 'Oruro',
  '500': 'Potosí',
  '600': 'Tarija',
  '700': 'Santa Cruz',
  '800': 'Beni',
  '900': 'Pando',
}