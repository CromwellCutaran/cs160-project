

//index page variables
var trackingNumber = document.getElementById("trackingNumberInput")
var clickButton  = document.getElementById("submitButton")

//console.log("in tracking")
//name.innerText = "Harkamal";

var data = null;

clickButton.addEventListener('click', sendTracking)


function sendTracking(e)
{
	e.preventDefault(); // prevent auto refresh maybe 
	if(trackingNumber.value != "")
	{
		var trackNumber = trackingNumber.value;

   $.ajax({
        url : "./post_tracking", // the endpoint
        type : "GET", // http method
        data : { tNumber : trackNumber,
            csrfmiddlewaretoken: '{{ csrf_token }}'
         }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#trackingNumberInput').val(''); // remove the value from the input
            console.log("tracking number sent back by server", json); // log the returned json to the console
          //  setTrackingPageValues(json);
          window.location.href = 'track';
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




