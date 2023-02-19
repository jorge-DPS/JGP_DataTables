"use strict";

// Class definition
var KTAccountSettingsSigninMethods = function () {
	// Private functions
	var initSettings = function () {

		// UI elements
		//var signInMainEl = document.getElementById('kt_signin_email');
		//var signInEditEl = document.getElementById('kt_signin_email_edit');
		var passwordMainEl = document.getElementById('kt_signin_password');
		var passwordEditEl = document.getElementById('kt_signin_password_edit');

		// button elements
		//var signInChangeEmail = document.getElementById('kt_signin_email_button');
		//var signInCancelEmail = document.getElementById('kt_signin_cancel');
		var passwordChange = document.getElementById('kt_signin_password_button');
		var passwordCancel = document.getElementById('kt_password_cancel');

		// toggle UI
		/*
		signInChangeEmail.querySelector('button').addEventListener('click', function () {
			toggleChangeEmail();
		});
		
		signInCancelEmail.addEventListener('click', function () {
			toggleChangeEmail();
		});
		*/

		passwordChange.querySelector('button').addEventListener('click', function () {
			toggleChangePassword();
		});

		passwordCancel.addEventListener('click', function () {
			toggleChangePassword();
		});
		/*
		var toggleChangeEmail = function () {
			signInMainEl.classList.toggle('d-none');
			signInChangeEmail.classList.toggle('d-none');
			signInEditEl.classList.toggle('d-none');
		}
		*/

		var toggleChangePassword = function () {
			passwordMainEl.classList.toggle('d-none');
			passwordChange.classList.toggle('d-none');
			passwordEditEl.classList.toggle('d-none');
		}
	}

	var handleChangeEmail = function (e) {
		var validation;

		// form elements
		var signInForm = document.getElementById('kt_signin_change_email');

		validation = FormValidation.formValidation(
			signInForm,
			{
				fields: {
						emailaddress: {
								validators: {
										notEmpty: {
												message: 'El correo electrónico nuevo es requerido'
										},
										emailAddress: {
												message: 'No es un correo valido'
										}
								}
						},

						confirmemailpassword: {
								validators: {
										notEmpty: {
												message: 'Se requiere la contraseña'
										}
								}
						}
				},

				plugins: { //Learn more: https://formvalidation.io/guide/plugins
					trigger: new FormValidation.plugins.Trigger(),
					bootstrap: new FormValidation.plugins.Bootstrap5({
						rowSelector: '.fv-row'
					})
				}
			}
		);

		signInForm.querySelector('#kt_signin_submit').addEventListener('click', function (e) {
			e.preventDefault();
			console.log('click');

			validation.validate().then(function (status) {
				swal.fire({
					text: "Se actualizará el correo electrónico. ¿estás seguro?",
					icon: "warning",
					buttonsStyling: false,
					confirmButtonText: "Aceptar!",
					customClass: {
						confirmButton: "btn font-weight-bold btn-light-primary"
					}
				}).then(function(){
					console.log("enviando datos de email para actualizar")
						
					if (status == 'Valid') {
						swal.fire({
							text: "Se ha actualizado el correo electrónico correctamente.",
							icon: "success",
							buttonsStyling: false,
							confirmButtonText: "Aceptar!",
							customClass: {
								confirmButton: "btn font-weight-bold btn-light-primary"
							}
						}).then(function(){
							console.log("enviando datos de email para actualizar")
							signInForm.reset();
							validation.resetForm(); // Reset formvalidation --- more info: https://formvalidation.io/guide/api/reset-form/
						});
					} else {
						swal.fire({
							text: "Lo sentimos, ha ocurrido un error con los datos introducidos, por favor revisa y prueba de nuevo.",
							icon: "error",
							buttonsStyling: false,
							confirmButtonText: "Aceptar!",
							customClass: {
								confirmButton: "btn font-weight-bold btn-light-primary"
							}
						});
					}
				});
			});
		});
	}

	var handleChangePassword = function (e) {
		var validation;

		// form elements
		var passwordForm = document.getElementById('kt_signin_change_password');

		validation = FormValidation.formValidation(
			passwordForm,
			{
				fields: {
						currentpassword: {
								validators: {
										notEmpty: {
												message: 'La contraseña actual es requerida'
										}
								}
						},

						newpassword: {
								validators: {
										notEmpty: {
												message: 'La nueva contraseña es requerida'
										}
								}
						},

						confirmpassword: {
								validators: {
										notEmpty: {
												message: 'Repita la nueva contraseña por favor'
										},
										identical: {
												compare: function() {
														return passwordForm.querySelector('[name="newpassword"]').value;
												},
												message: 'No coinside con la nueva contraseña'
										}
								}
						},
				},

				plugins: { //Learn more: https://formvalidation.io/guide/plugins
					trigger: new FormValidation.plugins.Trigger(),
					bootstrap: new FormValidation.plugins.Bootstrap5({
							rowSelector: '.fv-row'
					})
				}
			}
		);

		passwordForm.querySelector('#kt_password_submit').addEventListener('click', function (e) {
			e.preventDefault();
			console.log('click');

			validation.validate().then(function (status) {
				swal.fire({
						text: "Se actualizará tu contraseña. ¿estás seguro?",
						icon: "warning",
						buttonsStyling: false,
						confirmButtonText: "Aceptar!",
						customClass: {
							confirmButton: "btn font-weight-bold btn-light-primary"
						}
					}).then(function(){							
						if (status == 'Valid') {
							swal.fire({
								text: "Se ha actualizado tu contraseña.",
								icon: "success",
								buttonsStyling: false,
								confirmButtonText: "Aceptar!",
								customClass: {
									confirmButton: "btn font-weight-bold btn-light-primary"
								}
							}).then(function(){
								passwordForm.reset();
								validation.resetForm(); // Reset formvalidation --- more info: https://formvalidation.io/guide/api/reset-form/
							});
						} else {
							swal.fire({
								text: "Lo siento, ha ocurrido un error, revisa los campos de contraseña y prueba de nuevo.",
								icon: "error",
								buttonsStyling: false,
								confirmButtonText: "Aceptar!",
								customClass: {
									confirmButton: "btn font-weight-bold btn-light-primary"
								}
							});
						}
					});
			});
		});
	}

	// Public methods
	return {
		init: function () {
			initSettings();
			handleChangeEmail();
			handleChangePassword();
		}
	}
}();

// On document ready
KTUtil.onDOMContentLoaded(function() {
	KTAccountSettingsSigninMethods.init();
});
