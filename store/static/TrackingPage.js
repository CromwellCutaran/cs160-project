

//index page variables  (create element object)
var trackingNumber = document.getElementById("trackingNumberInput")
var clickButton  = document.getElementById("submitButton")

//console.log("in tracking")
//name.innerText = "Harkamal";

var data = null;
if(trackingNumber)
{
clickButton.addEventListener('click', sendTracking)
}

function sendTracking(e)
{
	e.preventDefault(); // prevent auto refresh maybe 
	if(trackingNumber.value != "")
	{
		var trackNumber = trackingNumber.value;

   $.ajax({ //This is the dictionary
        url : "./post_tracking", // the endpoint (where to send the data and goes to url the to views)
        type : "GET", // http method
        data : { tNumber : trackNumber, //what we sending 
            csrfmiddlewaretoken: '{{ csrf_token }}' //bypass secuirty permission
         }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#trackingNumberInput').val(''); // remove the value from the input
          //  console.log("tracking number sent back by server", json); // log the returned json to the console
          //  setTrackingPageValues(json);
          window.location.href = 'track'; //ocnce successfully data is sent then track is called in URL to Views
            console.log("success"); // another sanity check
        
        },

        // handle a non-successful response
        error : function(err)
        {
        	console.log("data could not be sent to server");
        }
        
    });
	}
	else 
	{	
	console.log("no input");
    alert("Please enter Tracking Number for your Order")
	}
	
}
//----------------------------------------------------------------------------
 //----------------------------------------------------------------------------
 //----------------------------------------------------------------------------
 


var addressLoc =  null;
var storeLoc = null;


function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: {lat: 37.56,  lng: -122.32} //santa clara 
  });
  directionsDisplay.setMap(map);
  //console.log("in initMap");
    calculateAndDisplayRoute(directionsService, directionsDisplay);
    calMidPoint(directionsService, directionsDisplay);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
   // console.log("in calculateAndDisplayRoute")
  directionsService.route({
    origin: $('#storeLoc').val() ,
    destination: $('#address').val(),
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}


function calMidPoint()
{
    console.log("calculating calMidPoint");
    var context = {
        origin: $('#storeLoc').val(),
        destination: $('#address').val(),
        travelMode: 'DRIVING'
    };

}

function sendLoc(data)
{
   addressLoc =  $('#address').val();
   storeloc =  $('#storeLoc').val();
    console.log(addressLoc);
    console.log(storeloc);
    //initMap()
}

document.addEventListener('DOMContentLoaded', sendLoc);


