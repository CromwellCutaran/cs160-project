from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import SM_produce, SC_produce
import pdb
import ast

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
#from store.models import Order #creating temp model to test traking page
from orders.models import OrderItems #refernce the database
from orders.models import Order

from django.db.models import Count
import pdb
#import simplejson as json
from django.core import serializers
import ast
import json as js
import datetime
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect



def index(request):
    #pdb.set_trace()
    return render(request, 'store/index0.html')

def products(request):

    location_id = request.path.split('_')[1]

    # TODO:
    # Restrict user from adding items from one store
    #  to cart as long as items from the other store
    #  are present in cart.


    if location_id == 'sc':
        location = 'SC_produceStore.html'
        db_products = SC_produce.objects.all().order_by("name")
    else:
        location = 'SM_produceStore.html'
        db_products = SM_produce.objects.all().order_by("name")

    request.session['store'] = location_id
    db_products_json = ast.literal_eval(serializers.serialize('json', db_products))
    
    # initialize cart in session
    if 'cart' not in request.session.keys():
        request.session['cart'] = { }

    context = {
        'db_products' : db_products_json,      
    }

    #pdb.set_trace()

    return render(request, "store/" + location, context)

def cart(request):

    # TODO:
    # Have two +/- buttons for quantity changing
    # Checkout button in bottom-right
    
    output = ""
    cart = request.session['cart']
    gen = (key for key in cart.keys() if key != 'location_id')
    for key in gen:
        output += (key + " " + "Quantity: " + str(cart[key][1]) + "<br/>")

    context = { 
        'cart' : cart,
        'location' : request.session['store'],
     }

    #pdb.set_trace()

    return render(request, 'store/cart.html', context)


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


    # TODO?:
    # Decrement cart items from database


    return HttpResponse("Cart updated")

def decrement_in_cart(request):

    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    item = request.POST['item']

    cart = request.session['cart']

    cart[item][1] = cart[item][1] - 1

    if cart[item][1] == 0: 
        cart.pop(item, None)

    return HttpResponse("Cart updated")

def increment_in_cart(request):

    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    item = request.POST['item']

    cart = request.session['cart']

    cart[item][1] = cart[item][1] + 1

    return HttpResponse("Cart updated")

def track(request):
    #context is dixtionary passed through the html page
    orderedItems = []
    orderedQuan = []
    itemDict = {}
    orderId = request.session.get('order_id')
    for e in OrderItems.objects.all():
        if e.order_id == orderId:
            orderedItems.append(e.item_id)
            orderedQuan.append(e.quantity)
    storeloc = request.session.get('loc')
    if storeloc == 'Santa Clara':
        #do stuff
        for i,q in zip(orderedItems,orderedQuan):
            tempOrder = SC_produce.objects.get(id=i).name
            quant = q
            itemDict[tempOrder] = quant
    
    else:
        for i,q in zip(orderedItems,orderedQuan):
            tempOrder = SM_produce.objects.get(id=i).name
            quant = q
            itemDict[tempOrder] = quant

        #do other stuff
    context = {
        'order_id' : orderId,
        'fname' : request.session.get('fname'),
        'lname' : request.session.get('lname'),
        'addr' :request.session.get('addr'),
        'city' : request.session.get('city'),
        'state' : request.session.get('state'),
        'loc' : storeloc,
        'price' : request.session.get('price'),
        'timestamp' : request.session.get('timestamp'),
        'zip' : request.session.get('zip'),
        'state' : request.session.get('state'),
        'email' : request.session.get('email'),
        'delivery' : request.session.get('delivery'),
        'progress_bar' : request.session.get('progress'),
        'items': itemDict

                }
    #pdb.set_trace()

    #request is the get 
   #pdb.set_trace()  render takes in template with what it will replace (context)
    return render(request, 'store/trackingPage.html', context) #renders the tracking page with the information 

@require_GET
@csrf_exempt #request is created 
def post_tracking(request): 
    if request.method == 'GET':#get from data base match the request
        tracking_number = request.GET.get('tNumber') #get the tracking number

        try:
            order = Order.objects.get(order_id=tracking_number) #set the table to order from the database

            request.session['order_id'] = order.order_id #saves in curretn session with key value pair 
            request.session['fname'] = order.first_name
            request.session['lname'] = order.last_name
            request.session['addr'] = order.address
            request.session['city'] = order.city
            request.session['state'] = order.state
            request.session['loc'] = order.location
            request.session['price'] = str(order.price_total)
            timeTemp = str(order.timestamp).split(".")[0]
            # pdb.set_trace()
            request.session['timestamp'] = timeTemp
            request.session['zip'] = order.zipcode
            request.session['state'] = order.state
            request.session['email'] = order.email
            delTemp = timeTemp.split(" ")[0]
            value = delTemp[0:8]
            orderdate = delTemp[8:10]
            dateUp = int(orderdate) + 2
            # pdb.set_trace()

            mylist = []
            today = datetime.date.today()
            mylist.append(today)
            currentDate=  str(mylist[0])
            currentDay = currentDate.split("-")[2]
            if int(currentDay) >= int(dateUp):
                request.session['progress'] = 100
            elif int(orderdate) == int(currentDay):
                request.session['progress'] = 0
            else: 
                request.session['progress'] = (int(dateUp) - int(currentDay))/(int(dateUp) - int(orderdate)) * 100
                #pdb.set_trace()
            if int(orderdate) == 30:
                dateUp = 1
                newMonth = int(value[5:7]) + 1
                value = value[0:5] + str(newMonth) + str('-')
                #pdb.set_trace()
            request.session['delivery'] = value + str(dateUp)
            #returns success response to AJAX which recieves the html page requests(includes sessions)
            return render(request, 'store/trackingPage.html')
        except Order.DoesNotExist:
            raise Http404("Order does not exist")
            