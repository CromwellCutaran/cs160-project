from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
#from store.models import Order #creating temp model to test traking page
from orders.models import OrderItems
from orders.models import Order
import pdb
import simplejson as json
from django.core import serializers
import ast
import json as js
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    #pdb.set_trace()
    return render(request, 'store/index0.html')

def track(request):
    t = loader.get_template('store/trackingPage.html')
    
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
    }
    
   #pdb.set_trace()
    return render(request, 'store/trackingPage.html', context)

@require_GET
@csrf_exempt
def post_tracking(request):	
    t = loader.get_template('store/trackingPage.html')
    data = {}
    if request.method == 'GET':#get from data base
        tracking_number = request.GET.get('tNumber')

       # return HttpResponse("SERVER: "+ tracking_number)
        try:
            order = Order.objects.get(order_id=tracking_number)
            
            request.session['order_id'] = order.order_id
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
            dateUp = delTemp[8:10]
            dateUp = int(dateUp) + 2
           # pdb.set_trace()

            request.session['delivery'] = value + str(dateUp)

            return render(request, 'store/trackingPage.html', data)
        except Order.DoesNotExist:
            raise Http404("Order does not exist")

