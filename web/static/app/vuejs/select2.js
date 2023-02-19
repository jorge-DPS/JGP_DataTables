$(".localidad").select2({ 
  ajax: { 
    url: "/api/v1/localidad", 
    dataType: 'json', 
    //delay: 250, 
    data: function (params) { 
      return { 
        search: params.term, 
        page: params.page 
      }; 
    }, 
    processResults: function (data, params) { 
      params.page = params.page || 1; 
      
      return { 
        results: $.map(data.results, function (d) { 
                   d.id = d.id; 
                   d.text = d.descripcion; 
                   return d; 
                  }), 
        pagination: { 
          more: data.next_page_url 
        } 
      }; 
    }, 
    cache: true 
  }, 
  "allowClear":true,"placeholder":"Zona","minimumInputLength":3, 
  escapeMarkup: function (markup) { 
      return markup; 
  } 
});

$(document).on('change', '.localidad', function() {
  var valorLocalidad= $('.localidad option:selected').val()
  app.zona.localidad = valorLocalidad;
});

/* $(document).on('change', ".localidad", function () { 
  var target = $(this).closest('.fields-group').find(".localidad"); 
  $.get("/api/v1/localidad",{search : this.value}, function (data) { 
      target.find("option").remove(); 
      $(target).select2({ 
          placeholder: {"id":"","text":""}, 
          allowClear: true, 
          data: $.map(data.results, function (d) { 
              d.id = d.id; 
              d.text = d.descripcion; 
              return d; 
          }) 
      }); 
      if ($(".localidad").val()) { 
          $(target).val(target.data('value')); 
          console.log($(".localidad").val());
          app.zona.localidad = $(".localidad").val();
      } 
      $(target).trigger('change'); 
  }); 
});


 */