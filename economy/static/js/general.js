function validations () {
    $("#txtValorProducto").keypress( function(event) {
        return validateNumericOnly(event);
    });
    $("#txtCuota").keypress( function(event) {
        return validateNumericOnly(event);
    });
    $("#txtNumeroCuotas").keypress( function(event) {
        return validateNumericOnly(event);
    });
}

function validateNumericOnly ( event ) {
    var key = event.which || event.keyCode;
    //alert(key)
    if ( ( key <= 57 && key >= 48 ) || ( key <= 40 && key >= 37 ) || key == 8 ) {
        return true;
    } else {
        return false;
    }
}

function calculate () {
    $.ajax({
        type: "POST",
        url: urlCalculateValues,
        data: { txtValorProducto: $("#txtValorProducto").val(),
            txtCuota: $("#txtCuota").val(),
            txtNumeroCuotas: $("#txtNumeroCuotas").val() }
    }).done(function( response ) {
        calbackCalculate(response);
    });
}

function calbackCalculate ( response ) {
    $("#showResult").html("Usted terminara pagando un total de: " + response.total_pay + " a una tasa de " + response.tax);
}

