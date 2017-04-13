from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
#from store.models import Order #creating temp model to test traking page
from orders.models import OrderItems #refernce the database
from orders.models import Order
import pdb
import simplejson as json
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

def track(request):
    #context is dixtionary passed through the html page
    context = {
    'order_id' : request.session.get('order_id'),
    'fname' : request.session.get('fname'),
    'lname' : request.session.get('lname'),
    'addr' :request.session.get('addr'),
    'city' : request.session.get('city'),
    'state' : request.session.get('state'),
    'loc' : request.session.get('loc'),
    'price' : request.session.get('price'),
    'timestamp' : request.session.get('timestamp'),
    'zip' : request.session.get('zip'),
    'state' : request.session.get('state'),
    'email' : request.session.get('email'),
    'delivery' : request.session.get('delivery'),
    'progress_bar' : request.session.get('progress')
    }
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
            if int(currentDay) > int(dateUp):
                request.session['progress'] = 100
            else: 
                request.session['progress'] = (int(dateUp) - int(currentDay))/(int(dateUp) - int(orderdate)) * 100
                #pdb.set_trace()

            request.session['delivery'] = value + str(dateUp)
            #returns success response to AJAX which recieves the html page requests(includes sessions)
            return render(request, 'store/trackingPage.html')
        except Order.DoesNotExist:
            raise Http404("Order does not exist")

