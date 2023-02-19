/*
$("#kt_daterangepicker_3").daterangepicker({
    singleDatePicker: true,
    showDropdowns: false,
    autoApply: true,
    timePicker: true,
    timePicker24Hour: true,
    locale: {
        format: 'DD/MM/YYYY',
        "separator": " - ",
        "applyLabel": "Aplicar",
        "cancelLabel": "Cancelar",
        "fromLabel": "De",
        "toLabel": "Hasta",
        "customRangeLabel": "Personalizar",
        "daysOfWeek": [
            "Lu",
            "Ma",
            "Mi",
            "Ju",
            "Vi",
            "Sa",
            "Do"
        ],
        "monthNames": [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Deciembre"
        ],
      },
    
  }
);

$("#kt_daterangepicker_3").on('apply.daterangepicker', function(ev, picker) {
    fecha = picker.startDate.format();
    app.deposito.fecha_deposito = fecha;
  });

  */
/*para buscar codigo de opreacion y nombre */
$('.js-data-example-ajax').select2({
  ajax: {
    url: "http://192.168.100.30:8003/api/v1/cre/creditos_activos",
    dataType: 'json',
    data: function (params) {
      return {
        q: params.term,
        page: params.page
      };
    },
    processResults: function (data, params) {
      params.page = params.page || 1;
      return {
        results: $.map(data.data, function (d) {
                  d.id = d.id;
                  d.text = d.text;
                  //console.log("codigo id", d.id)
                  return d;
                }),
        pagination: {
          more: data.next_page_url
        }
      };
    },
    cache: true
  },
  "allowClear": true,"placeholder":"Operacion","minimumInputLength":1,
  escapeMarkup: function (markup) {
      return markup;
  }
});


$(function () { $(document).off('change', ".oficina_creacion")
  $(document).on('change', ".oficina_creacion", function () {
    var target = $(this).find(".datos-asesor");
    $.get("http://192.168.100.30:8003/api/v1/adm/usuarios-sucursal",{q : this.value}, function (data) 
    {
      $("#agregar-asesor").empty().append('<option value="0">Seleccione una opcion  </option>');
      
      $(target).select2({
          
          placeholder: {"id":"","text":"Elegir"},
          data: $.map(data.data, function(  value, key ) {
            //console.log("value: ", value.text, "key: ", key)

            value.id = value.id;
            value.text = value.text;
            $( "#agregar-asesor" ).append( "<option value="+value.id +" selected='selected'>"+value.text+"</option>" );
            //$("#agregar-asesor > option[value="+value.id +"]").attr('selected', 'selected');
            return value;
          }),
          tags: true,
      });
   
      if (target.data('value')) {
          $(target).val(target.data('value'));
      }
      $(target).trigger('change');    
    });
    
  });
}); 

/*obtener valores de select-option operativo*/
$(document).on('change', '.valor-operacion', function() {
  var valorOperacion = $('.valor-operacion option:selected').val()
  app.deposito.codigo_operacion = valorOperacion;
});

/*obtener valores de select-option oficina*/
$(document).on('change', '.valor-oficina', function() {
  var valorOficina = $('.valor-oficina option:selected').val()
  
  app.deposito.sucursal_creacion = valorOficina;
});
/*obtener valores de select-option asesor*/
$(document).on('change', '.valor-asesor', function() {
  var valorAsesor = $('.valor-asesor option:selected').val()
  //var valorOption = $('.valor-asesor option:selected').text();
  app.deposito.codigo_asesor = valorAsesor;
  //app.nombreAsesor = valorOption;
  //console.log("valor Option", valorOption)
});
/*obtener valores de select-option banco*/
$(document).on('change', '.valor-banco', function() {
  var valorBanco = $('.valor-banco option:selected').val()
  app.deposito.banco = valorBanco;
});
/*obtener valores de select-option estado*/
$(document).on('change', '.valorEstado', function() {
  var valorEstado = $('.valorEstado option:selected').val()
  app.deposito.estado = valorEstado;
});
/*obtener valores de switch*/
$(document).on('change', '.valor-switch', function() {
  var valorSwitch = $('.valor-switch').is(":checked");
  app.deposito.estado = valorSwitch;
  console.log(valorSwitch)
});
