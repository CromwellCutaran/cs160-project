

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
 

 var polyline = null;
var addressLoc =  null;
var storeLoc = null;
var map;

function initMap() {
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;

map = new google.maps.Map(document.getElementById("map"));
    polyline = new google.maps.Polyline({
    path: [],
    strokeColor: '#FF0000',
    strokeWeight: 3
    });

  /* map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: {lat: 37.56,  lng: -122.32} //santa clara 
  });*/
  directionsDisplay.setMap(map);

  
  //console.log("in initMap");
    calculateAndDisplayRoute(directionsService, directionsDisplay);
    calMidPoint(directionsService, directionsDisplay, map);

    
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


function calMidPoint(directionsService, directionsDisplay, map)
{
    var geocoder = new google.maps.Geocoder();
    console.log("calculating calMidPoint");
    var context = {
        origin: $('#storeLoc').val(),
        destination: $('#address').val(),
        travelMode: 'DRIVING'
    };
       polyline.setPath([]);
    directionsService.route(context, function(response, status)
    {
    //var bounds = new google.maps.LatLngBounds();
        startLocation = new Object();
        endLocation = new Object();
        directionsDisplay.setDirections(response);
        var route = response.routes[0];
       // console.log("route stuff", route);
        var latX = route.legs[0].start_location.lat();
        var lngX = route.legs[0].start_location.lng();
        var latY =  route.legs[0].end_location.lat();
        var lngY =  route.legs[0].end_location.lng();
    var mid_lat = (latX + latY)/2;
 
    var  mid_lon = (latY + lngY)/2;
drawMarker(geocoder, map, mid_lat, mid_lon - 79.97);

    });



    

}

function drawMarker(geocoder, resultsMap, latt, lngg)
{
   
    var latlng = {lat: latt, lng: lngg};

            var marker = new google.maps.Marker({
              map: resultsMap,
              position: latlng
            });
 
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


