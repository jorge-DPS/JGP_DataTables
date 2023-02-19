var CSFR = { headers: { "X-CSRFToken": csrftoken } };

PASSWORD_MISTMATCH = "accounts.PasswordMistmatch";
INVALID_PASSWORD = "accounts.InvalidPassword";
BLANK = "blank";

let app = new Vue({
    el: "#vue_profile",
    data: {
        calendario: null,
        selected_profile: null,
        selected_password: null,
        info_content: null,
        pass_error: {
            password: null,
            new_password: null,
            confirm_password: null,
        },
        new_birtdate: "",
        user: {},
        passwordData: {
            oldpassword: { value: null, error: null },
            password1: { value: null, error: null },
            password2: { value: null, error: null }
        },
        opcion: {
            perfil: true,
            contrasena: false,
            edit: false,
            edit_contraseña: false,
        }
    },
    computed: {
      initials: function() {
        //console.log("datos computados", this.user.first_name.charAt(0), this.user.last_name.charAt(0));
        if (!!this.user.first_name){
          if (!!this.user.last_name){
            return ""+this.user.first_name.charAt(0) + this.user.last_name.charAt(0);
          } else {
            return this.user.first_name.charAt(0);
          }
        }else{
          return "USR";
        }
      },
    },
    methods: {
        toggleEdit: function() {
            if (!!this.opcion.edit){
                this.opcion.edit = false;
                this.opcion.perfil = true;
            }
            else{
                this.opcion.edit = true; 
                this.opcion.perfil = false;
            }
        },
        togglePasswordEdit: function(){
            if(!!this.opcion.edit_contraseña){
                this.opcion.edit_contraseña = false;
            }else {
                this.opcion.edit_contraseña = true;
            }
        },
        toogleMenuPassword: function() {
            this.opcion.contrasena = true;
            this.opcion.perfil = false;
            this.opcion.edit = false;
            this.selected_profile = "";
            this.selected_password = "active";
            
        },
        toogleMenuProfile: function() {
            this.opcion.perfil = true;
            this.opcion.contrasena = false; 
            this.opcion.edit = false;
            this.selected_profile = "active";
            this.selected_password = "";
        },
        cambiarContrasena: function() {
            //Borrar al implementar metronic8
            console.log("Cambiar Contraseña");
            this.opcion.perfil = false;
            this.opcion.contrasena = true;
            this.selected_profile = "";
            this.selected_password = "active";
        },

        cambiarPerfil: function() {
            //Borrar al implementar metronic8
            console.log("Cambiar Perfil");
            this.opcion.contrasena = false;
            this.opcion.perfil = true;
            this.selected_profile = "active";
            this.selected_password = "";
        },
        getProfile: function() {
            var url = URLS.endpoints.getProfile();
            //console.log("GET Profile", url);
            this.$http.get(url).then(
                function(response) {
                    this.user = response.body;
                    //console.log("PROFILE: ",response.body)
                },
                function(responseError) {
                    console.log("ERROR");
                    console.log(responseError);
                }
            );
        },

        makeProfileData: function () {
            //console.log("makeProfileData");
            var data = new FormData();
            if (!!this.user.username)
                data.append("username", this.user.username);

            if (!!this.user.first_name)
                data.append("first_name", this.user.first_name);

            if (!!this.user.last_name)
                data.append("last_name", this.user.last_name);

            if (!!this.user.phone)
                data.append("phone", this.user.phone);

            if (!!this.user.birthdate) {
                data.append("birthdate", this.user.birthdate);
            }

            if (!!this.user.incorporation_date) {
                //console.log("incorporation_date", this.user.incorporation_date);
                data.append("incorporation_date", this.user.incorporation_date);
            }

            if (!!this.$refs.avatarFile && this.$refs.avatarFile.files.length > 0) {
                //console.log("cargando avatar")
                data.append('avatar', this.$refs.avatarFile.files[0]);
            }
            return data;
        },

        updateProfile: function() {
            var data = this.makeProfileData();
            var url = URLS.endpoints.getProfile();

            this.$http.put(url, data, CSFR).then(function(response) {
                this.user = response.body;
                toastr.success("Perfil actualizado correctamente", "Actualizado", this.notification)
                this.toogleMenuProfile();
                //setTimeout(function() { location.reload() }, 500);
            }, function (responseError) {
                console.log("ERROR", responseError);
                toastr.error(responseError.body.message, "Error al actualizar", this.notification);
            });
        },

        clearSetPasswordData: function(clearValue) {
            this.setPasswordData.password.error = null;
            this.setPasswordData.confirm_password.error = null;

            if (clearValue) {
                this.setPasswordData.password.value = null;
                this.setPasswordData.confirm_password.value = null;
            }
        },

        clearPasswordData: function(clearValue) {
            this.passwordData.oldpassword.error = null;
            this.passwordData.password1.error = null;
            this.passwordData.password2.error = null;

            if (clearValue) {
                this.passwordData.oldpassword.value = null;
                this.passwordData.password1.value = null;
                this.passwordData.password2.value = null;
            }
        },

        updatePassword: function() {
            console.log("Change password")
            var data = {
                password: this.passwordData.oldpassword.value,
                new_password: this.passwordData.password1.value,
                confirm_password: this.passwordData.password2.value
            }
            this.$http.put(URLS.endpoints.putPassword(), data, CSFR).then(function(response) {
                this.clearPasswordData(true);
                //this.user = response.body;
                toastr.success("Contraseña actualizada correctamente", "Actualizado", this.notification);
                this.togglePasswordEdit();
            }, function(responseError) {
                this.clearPasswordData(false);
                this.setErrorPassword(responseError);
            });
        },

        setErrorPassword: function(responseError) {
            this.pass_error = responseError.body
            console.log(responseError);
            //TODO: realizar la validacion de pasword para que muestre alert si es q se introduce mal la contraseña actual
            console.log("caonsulta para passwor", !!responseError.body.password)
            if (!!responseError.body.password) {
                console.log("ERROR oldpassword", responseError.body.password[0].message)
                this.passwordData.oldpassword.error = responseError.body.password[0].message;
            } else {

                console.log("consulta para passwor1", !!responseError.body.new_password)
                if (!!responseError.body.new_password) {
                    console.log("ERROR password1", responseError.body.new_password[0].message)
                    this.passwordData.password1.error = responseError.body.new_password[0].message;
                } else {

                    console.log("consulta para passwor2", !!responseError.body.confirm_password)
                    if (!!responseError.body.confirm_password) {
                        console.log("ERROR pasword2")
                        this.passwordData.password2.error = responseError.body.confirm_password[0].message;
                    }
                }
            }
            if (responseError.body.errors.length > 0) {
                console.log("Error code: ", responseError.body.errors[0].message)
                switch (responseError.body.errors[0].code) {
                    case INVALID_PASSWORD || "accounts.InvalidPassword":
                        console.log("accounts.InvalidPassword:", responseError.body.errors[0].message);
                        this.passwordData.oldpassword.error = responseError.body.errors[0].message;
                        break;
                    case PASSWORD_MISTMATCH:
                        this.passwordData.password2.error = responseError.body.errors[0].message;
                        break;
                    case "accounts.PasswordMistmatch":
                        this.passwordData.password2.error = responseError.body.errors[0].message;
                        break;
                }
            }
        },
        calendar: function () {
            var self = this;
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
            var calendar = function () {
                // enable clear button
                $('#kt_datepicker_3, #kt_datepicker_3_validate').datepicker({
                    //rtl: KTUtil.isRTL(),
                    todayBtn: "linked",
                    clearBtn: true,
                    autoclose: true,
                    format: 'yyyy-mm-dd',
                    todayHighlight: true,
                    templates: arrows
                }).on("changeDate", function (ev) {
                    self.new_birtdate = ev.format(0, "yyyy-mm-dd");
                });
            }

            return {
                // public functions
                init: function () { calendar(); }
            };
        }
    },
    mounted: function() {
        this.info_content = $(this.$refs.info_content);
        this.selected_profile = "active";
        this.getProfile();
        //this.calendar().init();
    }
})