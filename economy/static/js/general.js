function calculate () {
    $.ajax({
        type: "GET",
        url: urlCalculateValues,
        data: { txtValorProducto: $("txtValorProducto").value }
    }).done(function( msg ) {
        alert( "Response " + msg );
    });
    //document.frmCalculte.action = urlCalculateValues;
    //document.frmCalculte.submit();
}
