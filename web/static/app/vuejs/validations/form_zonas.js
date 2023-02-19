// Define form element
const form = document.getElementById('kt_docs_formvalidation_text');
// Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
var validator = FormValidation.formValidation(
    form,
    {
        fields: {
            'text_input': {
                validators: {
                    notEmpty: {
                        message: 'Este campo "Descripcion Zonas" es requerido'
                    }
                }
            },
            'select2_input': {
                validators: {
                    notEmpty: {
                        message: 'Este campo "Localidad" es requerido'
                    }
                }
            },
        },

        plugins: {
            trigger: new FormValidation.plugins.Trigger(),
            bootstrap: new FormValidation.plugins.Bootstrap5({
                rowSelector: '.fv-row',
                eleInvalidClass: '',
                eleValidClass: ''
            })
        }
    }
);

// Submit button handler
const submitButton = document.getElementById('kt_docs_formvalidation_text_submit');
submitButton.addEventListener('mousedown', function (e) {
    // Prevent default button action
    e.preventDefault();

    //  app.zona.valor = validator.elements.select2_input[0].innerText
    // Validate form before submit
    if (validator) {
        validator.validate().then(function (status) {
            console.log('validated!');

            if (status == 'Valid') {
                // Show loading indication
                submitButton.setAttribute('data-kt-indicator', 'on');

                // Disable button to avoid multiple click
                submitButton.disabled = true;

                // Simulate form submission. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                setTimeout(function () {
                    // Remove loading indication
                    submitButton.removeAttribute('data-kt-indicator');

                    // Enable button
                    submitButton.disabled = false;

                    // Show popup confirmation
                    

                    //form.submit(); // Submit form
                });
            }
        });
    }
});

/* =================0 itemSelect2 ====================*/
   


