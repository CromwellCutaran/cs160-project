

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
 var timestamp = null;
 var map;

 function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;

  map = new google.maps.Map(document.getElementById('map'), mapOps = {
      zoom: 7,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      center: {lat: 37.56,  lng: -122.32} //santa clara
  });
  
  directionsDisplay.setMap(map);
  calculateAndDisplayRoute(directionsService, directionsDisplay); 
}



function calculateAndDisplayRoute(directionsService, directionsDisplay) {
var context = {
    origin: $('#storeLoc').val(),
    destination: $('#address').val(),
    travelMode: 'DRIVING'
};

directionsService.route(context, function(response, status)
{
    if (status === 'OK') {
       
        directionsDisplay.setDirections(response);
        // For each route, display summary information.
        var legs = response.routes[0].legs;
         marker = drawMarker(legs[0].start_location);




         var splitTime = timestamp.split(" ")
         console.log(splitTime)
         var dayOfPurch = splitTime[0].split("-")[2] //date of pruchase
        
        var today = new Date();
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
       var todayDay = date.split('-')[2] //todays date
       
       var stepsLength = legs[0].steps.length
       
       var stepper = null

       //console.log(dayOfPurch)
       var stepCheck = stepsLength -1 
       if (parseInt(dayOfPurch) === parseInt(todayDay))
       {
         
        console.log("in equal "  + stepCheck)
       }
        else if ((parseInt(dayOfPurch) +1) ===(parseInt(todayDay)))
       {
         stepCheck = Math.floor(Math.random() * (stepsLength/3)) + 1 
         console.log(stepsLength/2)

       }
        else if ((parseInt(dayOfPurch) + 2) ===  parseInt(todayDay))
       {
         stepCheck = stepsLength -1 

       }
        
      console.log(stepCheck)
        var lattt = legs[0].steps[stepCheck].end_location.lat();
        var lnggg = legs[0].steps[stepCheck].end_location.lng();
        var latlng = {lat: lattt, lng: lnggg};
        drawMarker(latlng);
        
    }
    else {
        alert("directions response "+status);
    }
 });
}


function drawMarker(latlng)
{
    //console.log("in drawMarker")

    var marker = new google.maps.Marker({
      map: map,
      position: latlng
  });

}

function sendLoc(data)
{
 addressLoc =  $('#address').val();
 storeloc  =  $('#storeLoc').val();
 timestamp =$('#timeBought').val();
 console.log(addressLoc);
 console.log(storeloc);
 console.log(timestamp)
}

document.addEventListener('DOMContentLoaded', sendLoc);


