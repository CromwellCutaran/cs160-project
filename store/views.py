from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'store/index0.html')


def track(request):
    return render(request, 'store/trackingPage.html')

def post(request):
	if request.method == 'POST':
		tracking_number = request.POST.get('tNumber')
		return HttpResponse(
			json.dumps(tracking_number),
            content_type="application/json"
            )
            

'''
def get_trackingNumber(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TrackPage(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('//')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TrackPage()

    return render(request, 'track.html', {'form': form})
    '''