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
            #order = list(Order.objects.get(order_id=tracking_number))
            #db_order_json = ast.literal_eval(serializers.serialize('json', order))
            order = Order.objects.get(order_id=tracking_number)
           
            data['order_id'] = order.order_id
            data['fname'] = order.first_name
            data['lname'] = order.last_name
            data['addr'] = order.address
            data['city'] = order.city
            data['state'] = order.state
            data['loc'] = order.location
            data['price'] = order.price_total
            data['timestamp'] = str(order.timestamp)
            data['zip'] = order.zipcode
            data['state'] = order.state
            data['email'] = order.email
            data['delivery'] = str(order.timestamp)
            json_data = json.dumps(data)
            jsonTemp = json_data
           # pdb.set_trace()
            '''
            context = {'fname': order.first_name,
            'lname': order.last_name,
            'timestamp': str(order.timestamp),
            'loc' : order.location,
            'addr' : order.address,
            'city' : order.city,
            'state' : order.state,
            'zip' : order.zipcode,
            'email': order.email,
            'delivery': str(order.timestamp),
            'price': order.price,
            }
            '''
            request.session['order_id'] = order.order_id
            request.session['fname'] = order.first_name
            request.session['lname'] = order.last_name
            request.session['addr'] = order.address
            request.session['city'] = order.city
            request.session['state'] = order.state
            request.session['loc'] = order.location
            request.session['price'] = str(order.price_total)
            request.session['timestamp'] = str(order.timestamp)
            request.session['zip'] = order.zipcode
            request.session['state'] = order.state
            request.session['email'] = order.email
            request.session['delivery'] = str(order.timestamp)

            return render(request, 'store/trackingPage.html', data)
        except Order.DoesNotExist:
            raise Http404("Order does not exist")


