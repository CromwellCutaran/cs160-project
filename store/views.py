from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import SM_produce, SC_produce
import pdb
import ast

def index(request):
    return render(request, 'store/index0.html')

def products(request):
    location = 'SC_produceStore.html' if request.path.split('_')[1] == 'sc' \
        else 'SM_produceStore.html'
    db_products = SC_produce.objects.all() if request.path.split('_')[1] == 'sc' \
        else SM_produce.objects.all()
    db_products_json = ast.literal_eval(serializers.serialize('json', db_products))
    context = {
        'db_products' : db_products
    }
    pdb.set_trace()
    return render(request, "store/" + location, context)

def tracking(request):
    return HttpResponse("Tracking")

def update_cart(request):
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    request.session['m']