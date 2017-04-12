
//tracking page variables 

console.log("in page 2")
/*
var name = document.getElementById("name");
var date_purchased = document.getElementById("date-purchased");
var store_location = document.getElementById("store-location");
var shippingAddr = document.getElementById("shippingAddr");
var conf_email = document.getElementById("conf-email");
var exp_arrival = document.getElementById("exp-arrival");
var amt_paid = document.getElementById("amt-paid");

*/


//setting tracking page values 
function setTrackingPageValues(json)
{
    console.log("in setTrackingPageValues" + json)
  /*  var data = JSON.parse(json);
    name.value = data['first_name'] + ' ' + data['last_name'];
    date_purchased.value = data['timestamp']
    store_location.innerText = date['store_location']
    shippingAddr.innerText = data['address'] + ' ' + data['city'] + ' ' + data['state'] + ' ' + data['zipcode']
    conf_email.innerText = data['email']
    //exp_arrival.data = data['']
    amt_paid.innerText = data['price']

*/

    var data = JSON.parse(json);
    $("#name").text(data['first_name'] + ' ' + data['last_name']);
    $("#data-purchased").val(data['timestamp']);
    $("#store-location").val(data['store_location']);
    $("#shippingAddr").val( data['address'] + ' ' + data['city'] + ' ' + data['state'] + ' ' + data['zipcode']);
    $("#conf-email").val(data['email']);
    $("#exp-arrival").val("2");
    $("#amt-paid").val(data['price']);
    

    window.location.href = "track";


}


//setTrackingPageValues(data);





