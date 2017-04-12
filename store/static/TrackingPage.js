

//index page variables
var trackingNumber = document.getElementById("trackingNumberInput")
var clickButton  = document.getElementById("submitButton")

//console.log("in tracking")
//name.innerText = "Harkamal";

var data = null;

clickButton.addEventListener('click', sendTracking)


function sendTracking(e)
{
	e.preventDefault();
	if(trackingNumber.value != "")
	{
		var trackNumber = trackingNumber.value;
    
	console.log("sending trackNumber to server....");
   $.ajax({
        url : "./track", // the endpoint
        type : "GET", // http method
        data : { 'tNumber' : trackNumber,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
         }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#trackingNumberInput').val(''); // remove the value from the input
            console.log("tracking number sent back by server", json); // log the returned json to the console
            //setTrackingPageValues(trackNumber);
            console.log("success"); // another sanity check
             //window.location.href = "track";
        
        },

        // handle a non-successful response
        error : function(err)
        {
        	console.log("data could not be sent to server");
        }
        
    });
    //getData(trackNumber);

	}
	else 
	{	
	console.log("no input");
	}
	
}


//setting tracking page values 
function setTrackingPageValues(json)
{
    console.log("setting values for tracking page")
    var data = JSON.parse(json);
    $("#name").val(data['first_name'] + ' ' + data['last_name']);
    $("#data-purchased").val(data['timestamp']);
    $("#store-location").val(data['store_location']);
    $("#shippingAddr").val( data['address'] + ' ' + data['city'] + ' ' + data['state'] + ' ' + data['zipcode']);
    $("#conf-email").val(data['email']);
    
    $("#amt-paid").val(data['price']);
    
    console.log(" expected time: ",$("#exp-arrival").val());

   /* name.innerText = data['first_name'] + ' ' + data['last_name'];
    date_purchased.innerText = data['timestamp']
    store_location.innerText = date['store_location']
    shippingAddr.innerText = data['address'] + ' ' + data['city'] + ' ' + data['state'] + ' ' + data['zipcode']
    conf_email.innerText = data['email']
    //exp_arrival.data = data['']
    amt_paid.innerText = data['price']
*/
    window.location.href = "track";


}




