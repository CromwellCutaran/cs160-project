var trackingNumber = document.getElementById("trackingNumberInput")
var clickButton  = document.getElementById("submitButton")

clickButton.addEventListener('click', sendTracking)

function sendTracking(e)
{
	e.preventDefault();
	if(trackingNumber.value != "")
	{
		var trackNumber = trackingNumber.value;
	console.log("in sendTracking " + trackingNumber.value);
	window.location.href = "trackingPage.html";
	console.log("sending trackNumber to server");
  /* $.ajax({
        url : "post", // the endpoint
        type : "POST", // http method
        data : { tNumber : trackNumber }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#trackingNumberInput').val(''); // remove the value from the input
            console.log("tracking number sent back by server",json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(err)
        {
        	console.log("data could not be sent to server");
        }
        
    });*/

	}
	else 
	{	
	console.log("no input");
	}
	
}
