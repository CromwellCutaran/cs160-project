from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import SM_produce, SC_produce
import pdb
import ast

def index(request):
    return render(request, 'store/index0.html')

def products(request):

    location_id = request.path.split('_')[1]

    # TODO:
    # Restrict user from adding items from one store
    #  to cart as long as items from the other store
    #  are present in cart.


    if location_id == 'sc':
        location = 'SC_produceStore.html'
        db_products = SC_produce.objects.all()
    else:
        location = 'SM_produceStore.html'
        db_products = SM_produce.objects.all()

    request.session['store'] = location_id
    db_products_json = ast.literal_eval(serializers.serialize('json', db_products))
    
    # initialize cart in session
    if 'cart' not in request.session.keys():
        request.session['cart'] = { }

    context = {
        'db_products' : db_products_json      
    }

    #pdb.set_trace()

    return render(request, "store/" + location, context)

def cart(request):
    output = ""
    cart = request.session['cart']
    gen = (key for key in cart.keys() if key != 'location_id')
    for key in gen:
        output += (key + " " + "Quantity: " + str(cart[key][1]) + "<br/>")
    #pdb.set_trace()
    return HttpResponse(output)


def tracking(request):
    return HttpResponse("Tracking")

def update_cart(request):
    # When the user adds their firt item,
    #  set the location session variable

    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    fields = ast.literal_eval(request.POST['item'])
    cart = request.session['cart']


    # Cart data format:
    # request.session['cart'] = {
    #  item1 : [{...fields1...}, quantity1],
    #  item2 : [{...fields2...}, quantity2],
    #  ... }

    # Instantiate if item is not yet in cart
    if fields['name'] not in cart.keys():
        cart.update({fields['name'] : [fields, 1]})
    # Otherwise increment item
    else:
        cart[fields['name']][1] += 1

    request.session['cart'] = cart

    return HttpResponse("Cart updated")