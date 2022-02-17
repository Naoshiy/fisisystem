function gohome(){
    window.location='form1.html';
}
function save(){
    window.localStorage.setItem('#id_bill_of_land', $('#id_bill_of_land').val());
}
function load(){
    $('#id_bill_of_land').val(window.localStorage.getItem('#id_bill_of_land'));
}
function erase(){
    window.localStorage.removeItem('#id_bill_of_land');
}


// function gohome(){
//     window.location='form1.html';
// }
// function save(){
//     window.localStorage.setItem('campo1', $('#campo1').val());
// }
// function load(){
//     $('#campo2').val(window.localStorage.getItem('campo1'));
// }
// function erase(){
//     window.localStorage.removeItem('campo1');
// }