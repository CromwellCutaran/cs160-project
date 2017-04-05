from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'store/index0.html')

def products(request):
    location = 'Santa Clara' if request.path.split('_')[1] == 'sc' \
        else 'San Mateo'
    return HttpResponse("Products for " + location + " location")

def tracking(request):
    return HttpResponse("Tracking")
    
