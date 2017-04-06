from django.shortcuts import render
from django.http import HttpResponse
from .models import SM_produce


def index(request):
    return render(request, 'store/index0.html')

def products(request):
    location = 'SC_produceStore.html' if request.path.split('_')[1] == 'sc' \
        else 'SM_produceStore.html'
    return render(request, "store/" + location)

def tracking(request):
    return HttpResponse("Tracking")
