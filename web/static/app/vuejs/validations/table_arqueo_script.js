
var footer = true;
function edit_row(no) {
  document.getElementById("edit_button" + no).style.display = "none";
  document.getElementById("save_button" + no).style.display = "inline-block";
  
  var cod_corte = document.getElementById("cod_corte_moneda_row" + no);
  var cant_corte = document.getElementById("cant_corte_moneda_row" + no);
  var valor_corte = document.getElementById("valor_corte_moneda_row" + no);
  var sub_total = document.getElementById("sub_total_row" + no);
  
  var cod_corte_data = cod_corte.innerHTML;
  var cant_corte_data = cant_corte.innerHTML;
  var valor_corte_data = valor_corte.innerHTML;
  //var sub_total_data = sub_total.innerHTML

  
  cod_corte.innerHTML =
  "<div class='col-xs-2'>\n\
  <input class='form-control' type='text' id='name_text" + no + "' value='" + cod_corte_data + "' onfocusout='focusInput(" + no + ")'>\n\
  </div>";
 //"<input type='text' id='name_text" + no + "' value='" + cod_corte_data + "'>";
 cant_corte.innerHTML =
  "<div class='col-xs-2'>\n\
  <input class='form-control' type='text' id='country_text" + no + "' value='" + cant_corte_data + "' onfocusout='focusInput(" + no + ")'>\n\
  </div>";
  //"<input type='text' id='country_text" + no + "' value='" + cant_corte_data + "'>";
  valor_corte.innerHTML =
  "<div class='col-xs-2'>\n\
  <input class='form-control' type='text' id='age_text" + no + "' value='" + valor_corte_data + "' onfocusout='focusInput(" + no + ")'>\n\
  </div>";

  /* sub_total.innerHTML=
  "<div class='col-xs-2'>\n\
  <span class='fw-bold fs-6 text-gray-400' type='text' id='sub_total_text" + no + "'>" + cod_corte_data * cant_corte_data * valor_corte_data + "</span>\n\
  </div>"; */

  //var valorSave = document.getElementById("sub_total_text" + no) .innerHTML

  //var subTotalValor = document.getElementById("sub_total_valor0")
  //var subTotalValor_data_cero = subTotalValor.innerHTML
  
  //"<input type='text' id='age_text" + no + "' value='" + valor_corte_data + "'>";
}

function save_row(no) {
  var name_val = document.getElementById("name_text" + no).value;
  var country_val = document.getElementById("country_text" + no).value;
  var age_val = document.getElementById("age_text" + no).value;
  var sub_total_val = document.getElementById("sub_total_row" + no).innerHTML
  // suma del con el campo editado
  var subTotalValor = document.getElementById("sub_total_valor0")
  var subTotalValor_data_cero = subTotalValor.innerHTML

  subTotalValor.innerHTML = (parseFloat(subTotalValor_data_cero) - parseFloat(sub_total_val)).toFixed(2)
  var new_valor = subTotalValor.innerHTML = (parseFloat(subTotalValor_data_cero) - parseFloat(sub_total_val))
  document.getElementById("cod_corte_moneda_row" + no).innerHTML = name_val;
  document.getElementById("cant_corte_moneda_row" + no).innerHTML = country_val;
  document.getElementById("valor_corte_moneda_row" + no).innerHTML = age_val;
  document.getElementById("sub_total_row" + no).innerHTML = (name_val * country_val * age_val).toFixed(2);
  
  var sub_total_val = document.getElementById("sub_total_row" + no).innerHTML
  
  subTotalValor.innerHTML = (parseFloat(new_valor) + parseFloat(sub_total_val)).toFixed(2)

  document.getElementById("edit_button" + no).style.display = "inline-block";
  document.getElementById("save_button" + no).style.display = "none";
}

function delete_row(no) {
  var sub_total_val = document.getElementById("sub_total_row" + no).innerHTML
  var subTotalValor = document.getElementById("sub_total_valor0")
  var subTotalValor_data_cero = subTotalValor.innerHTML
  
  subTotalValor.innerHTML = (parseFloat(subTotalValor_data_cero) - parseFloat(sub_total_val)).toFixed(2)
  document.getElementById("row" + no + "").outerHTML = "";

}

function add_row() {
  var cod_corte_moneda   = document.getElementById("cod_corte_moneda").value;
  var new_country = document.getElementById("new_country").value;
  var new_age = document.getElementById("new_age").value;
  
  var table = document.getElementById("data_table");
  var table_len = table.rows.length - 1;
  var row = (table.insertRow(table_len).outerHTML =
    "<tr id='row" +
    table_len +
    "'><td>\n\
    <span class='fw-bold fs-6 text-gray-400' style='width: 15%;' id='cod_corte_moneda_row" + table_len +"'>"+ cod_corte_moneda +"</span>"+
    "</td><td>\n\
    <span class='fw-bold fs-6 text-gray-400' style='width: 15%;' id='cant_corte_moneda_row" + table_len +"'>"+ new_country +"</span>"+ 
    "</td><td>\n\
    <span class='fw-bold fs-6 text-gray-400' style='width: 15%;' id='valor_corte_moneda_row" + table_len +"'>"+ new_age +"</span>"+
    "</td>\n\
    <td>\n\
    <span class='fw-bold fs-6 text-gray-400' style='width: 15%;' id='sub_total_row" + table_len +"'>"+ (cod_corte_moneda * new_country * new_age).toFixed(2) +"</span>"+
    "</td>\n\
    <td><button class='btn btn-sm btn-light btn-active-primary btn-icon m-1' title='Editar' id='edit_button" +
    table_len +
    "' value='Edit' onclick='edit_row(" +
    table_len +
    ")'><i class='bi bi-pencil-square'></i></button>\n\
    <button class='save btn btn-sm btn-light btn-active-primary btn-icon m-1' title='Guardar' id='save_button" +
    table_len +
    "' value='Save' onclick='save_row(" +
    table_len +
    ")'><i class='bi bi-check-square'></i>\n\
    </button><button class='btn btn-sm btn-light-danger btn-active-danger btn-icon m-1' title='Eliminar' onclick='delete_row(" +
    table_len +
    ")'><i class='bi bi-trash'></i></button></td></tr>");
    
    $(".save").css('display', 'none')
    document.getElementById("cod_corte_moneda").value = "";
    document.getElementById("new_country").value = "";
    document.getElementById("new_age").value = "";
    if (0 == table_len) {
      var table = document.getElementById("myTable");
      var footer = table.createTFoot();
      var row = footer.insertRow(0);
      var cell = row.insertCell(0);
      var cell1 = row.insertCell(1);
      var cell2 = row.insertCell(2);
      var cell3 = row.insertCell(3);
      cell.innerHTML = "<b>Total</b>";
      cell3.innerHTML =  "<div class='col-xs-2'>\n\
      <span class='fw-bold fs-6 text-gray-400' type='text' id='sub_total_valor0'>" + 0 + "</span>\n\
      </div>";
    }

    var subTotalValor = document.getElementById("sub_total_valor0")
    var subTotalValor_data_cero = subTotalValor.innerHTML
    var subTotalValor_row = document.getElementById("sub_total_row" + table_len)

    var subTotalValor_data = subTotalValor_row.innerHTML

    //document.getElementById("sub_total_valor0").innerHTML = subTotalValor;
    subTotalValor.innerHTML = (parseFloat(subTotalValor_data_cero) + parseFloat(subTotalValor_data)).toFixed(2)

  }
  
  //onfocusout Event-> cuando se sale del foco del input
  function focusInput(no) {
    /* var x = document.getElementById("fname");
    x.value = x.value.toUpperCase(); */
    save_row(no)
  }