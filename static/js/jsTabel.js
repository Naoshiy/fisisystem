function cadMaterial(store, PO_number,receiving_material, sidemark, roll_number, Qty_Sy, width, length){
    var tb = document.getElementById("table-list");
    var qntLinhas = tb.insertRow.length;
    var linha = tb.insertRow(qntLinhas);
    var cellCodigo = linha.insertCell(0);
    var cellStore = linha.insertCell(1);
    var cellPO_number = linha.insertCell(2);
    var cellReceiving_material = linha.insertCell(3);
    var  cellSidemark = linha.insertCell(4);
    var cellRoll_number = linha.insertCell(5);
    var cellQty_Sy = linha.insertCell(6);
    var cellWidth = linha.insertCell(7);
    var cellLength = linha.insertCell(8);

    cellCodigo.innerHTML = qntLinhas;
    cellStore.innerHTML = store ;
    cellPO_number = PO_number ;
    cellReceiving_material = sidemark ;
    cellSidemark = receiving_material ;
    cellRoll_number = roll_number ;
    cellQty_Sy = Qty_Sy ;
    cellWidth = width ;
    cellLength = length ;
}

$('#mat').on('click', function(){
    adicionarItemTable();
  });
  
  function adicionarItemTable() {
  
              var POnumber = $('#id_product-0-PO_number').val();
              var ordernumber     = $('#id_product-0-Order_number').val();
              var SideMark = $('#id_product-0-Side_Mark').val();
              var Carrier = $('#id_product-0-carrier').val();
              var RollNumber = $('#id_product-0-Roll_number').val();
  
              var linha = "" +
                  "<tr>" +
                     "<td>"+POnumber+"</td>"+
                     "<td>"+ordernumber+"</td>"+
                     "<td>"+SideMark+"</td>"+
                     "<td>"+Carrier+"</td>"+
                     "<td>"+RollNumber+"</td>"+
                  "  <td><a href='#' class='btn btn-danger btn-remove btn-xs'>remover</a></td>"+
                  "</tr>";
              $('.tbody').append( linha );
              $('#id_product-0-PO_number').val('');
              $('#id_product-0-Order_number').val('');
              $('#id_product-0-Side_Mark').val('');
              $('#id_product-0-carrier').val('');
              $('#id_product-0-Roll_number').val('');
  
          }
          
          $(".tbody").on("click", ".btn-remove", function(e){
              $(this).closest('tr').remove();
              
          });