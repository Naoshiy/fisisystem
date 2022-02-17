



$(document).ready(function(){
    $("#add-item").click(function(ev) {
        ev.preventDefault();
        var count = $('#order').children().length; // div do forms - pode excluir
        var tmplMarkup = $("#item-order").html(); //script de troca
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $("div#order").append(compiledTmpl);

        // update form count
        $('#id_product-TOTAL_FORMS').attr('value', count + 1);

        // --------------- function with iteration----------------------

    $("#mat").click(function(){               
        var POnumber = $('#id_product-'+ '#order' +'-PO_number').val().append(compiledTmpl);
        var ordernumber = $('#id_product-order-Order_number').val();
        var SideMark = $('#id_product-order-Side_Mark').val();
        var Carrier = $('#id_product-order-carrier').val();
        var RollNumber = $('#id_product-order-Roll_number').val();
        var width = $('#id_product-order-width').val();
        var length = $('#id_product-order-length').val();
        var Quantity = $('#id_product-order-Quantity').val();
        var MaterialType = $('#id_product-order-material_type').val();
        var store = $('#id_product-order-store').val();

        var linha = "" +
            "<tr>" +
            "<td>"+POnumber+"</td>"+
            "<td>"+ordernumber+"</td>"+
            "<td>"+SideMark+"</td>"+
            "<td>"+Carrier+"</td>"+
            "<td>"+RollNumber+"</td>"+
            "<td>"+width+"</td>"+
            "<td>"+length+"</td>"+
            "<td>"+Quantity+"</td>"+
            "<td>"+MaterialType+"</td>"+
            "<td>"+store+"</td>"+
            "  <td><a href='#' class='btn btn-danger btn-remove btn-xs'>remover</a></td>"+
            "</tr>";
        $('#table-list').append( linha );    
        $('#id_product-'+'#order'+'-PO_number').val('').append(compiledTmpl);;
        $('#id_product-order-Order_number').val('');
        $('#id_product-order-Side_Mark').val('');
        $('#id_product-order-carrier').val('');
        $('#id_product-order-Roll_number').val('');
        $('#id_product-order-width').val('');
        $('#id_product-order-length').val('');
        $('#id_product-order-Quantity').val('');
        $('#id_product-order-material_type').val('');}
});
// ------------------final function with iteration------------------
        <script type="text/html" id="item-order">
        <div id="item-__prefix__" style="margin-top: 10px">
                {{ formset.empty_form|crispy }}
        </div>
    </script>


            // --------------- function with iteration----------------------
            $("#mat").click(function(){
                var POnumber = $('#id_product-0-PO_number').val();
                var ordernumber = $('#id_product-0-Order_number').val();
                var SideMark = $('#id_product-order-Side_Mark').val();
                var Carrier = $('#id_product-order-carrier').val();
                var RollNumber = $('#id_product-order-Roll_number').val();
                var width = $('#id_product-order-width').val();
                var length = $('#id_product-order-length').val();
                var Quantity = $('#id_product-order-Quantity').val();
                var MaterialType = $('#id_product-order-material_type').val();
                var store = $('#id_product-order-store').val();
                
                var linha = "" +
                    "<tr>" +
                    "<td>"+POnumber+"</td>"+
                    "<td>"+ordernumber+"</td>"+
                    "<td>"+SideMark+"</td>"+
                    "<td>"+Carrier+"</td>"+
                    "<td>"+RollNumber+"</td>"+
                    "<td>"+width+"</td>"+
                    "<td>"+length+"</td>"+
                    "<td>"+Quantity+"</td>"+
                    "<td>"+MaterialType+"</td>"+
                    "<td>"+store+"</td>"+
                    "  <td><a href='#' class='btn btn-danger btn-remove btn-xs'>remover</a></td>"+
                    "</tr>";
                $('#table-list').append( linha );    
                $('#id_product-0-PO_number').val('');
                $('#id_product-0-Order_number').val('');
                $('#id_product-order-Side_Mark').val('');
                $('#id_product-order-carrier').val('');
                $('#id_product-order-Roll_number').val('');
                $('#id_product-order-width').val('');
                $('#id_product-order-length').val('');
                $('#id_product-order-Quantity').val('');
                $('#id_product-order-material_type').val('');
        });
        // ------------------final function with iteration------------------













// ---------- original function---------------
function adicionarItemTable() {
    var POnumber = $('#id_product-0-PO_number').val();
    var ordernumber     = $('#id_product-0-Order_number').val();
    var SideMark = $('#id_product-0-Side_Mark').val();
    var Carrier = $('#id_product-0-carrier').val();
    var RollNumber = $('#id_product-0-Roll_number').val();
    var width = $('#id_product-0-width').val();
    var length = $('#id_product-0-length').val();
    var Quantity = $('#id_product-0-Quantity').val();
    var MaterialType = $('#id_product-0-material_type').val();
    var store = $('#id_product-0-store').val();

    var linha = "" +
        "<tr>" +
           "<td>"+POnumber+"</td>"+
           "<td>"+ordernumber+"</td>"+
           "<td>"+SideMark+"</td>"+
           "<td>"+Carrier+"</td>"+
           "<td>"+RollNumber+"</td>"+
           "<td>"+width+"</td>"+
           "<td>"+length+"</td>"+
           "<td>"+Quantity+"</td>"+
           "<td>"+MaterialType+"</td>"+
           "<td>"+store+"</td>"+
           "  <td><a href='#' class='btn btn-danger btn-remove btn-xs'>Remove</a></td>"+
        "</tr>";
    $('.tbody').append( linha );
    $('#id_product-0-PO_number').val('');
    $('#id_product-0-Order_number').val('');
    $('#id_product-0-Side_Mark').val('');
    $('#id_product-0-carrier').val('');
    $('#id_product-0-Roll_number').val('');
    $('#id_product-0-width').val('');
    $('#id_product-0-length').val('');
    $('#id_product-0-Quantity').val('');
    $('#id_product-0-material_type').val('');
    $('#id_product-0-store').val('');
}
// ------------------final function principal------------------


// atualiza div
$("#btn-bill").click(function(){
    $( "#div1" ).load("forms1.html", #table-bill);});
    });





