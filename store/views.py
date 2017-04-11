from django.shortcuts import render
from django.http import HttpResponse
from .models import SM_produce, SC_produce


def index(request):
    return render(request, 'store/index0.html')

def products(request):
    location = 'SC_produceStore.html' if request.path.split('_')[1] == 'sc' \
        else 'SM_produceStore.html'
    db_products = SC_produce.objects.all() if request.path.split('_')[1] == 'sc' \
        else SM_produce.objects.all()
    context = {
        'db_products' : db_products,
    }
    print(db_products)
    return render(request, "store/" + location, context)

def tracking(request):
    return HttpResponse("Tracking")
