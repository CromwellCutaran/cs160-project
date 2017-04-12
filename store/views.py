from django.shortcuts import render
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




jsonTemp = None



def index(request):
    return render(request, 'store/index0.html')

@require_GET
@csrf_exempt
def track(request):
 #  tracking_number = request.GET.get('tNumber')
    ''' 
    order = Order.objects.get(order_id=tracking_number)
    data = {}
    data['order_id'] = order.order_id
    data['first_name'] = order.first_name
    data['last_name'] = order.last_name
    data['address'] = order.address
    data['city'] = order.city
    data['state'] = order.state
    data['store_location'] = order.location
    data['price'] = order.price_total
    data['timestamp'] = str(order.timestamp)
    data['zipcode'] = order.zipcode
    data['state'] = order.state
    data['email'] = order.email
    '''
    if request.method == 'GET':
        return render(request, 'store/trackingPage.html', {"fname": request.GET.get('tNumber')})

@require_GET
@csrf_exempt
def post_tracking(request):	
    if request.method == 'GET':#get from data base
        tracking_number = request.GET.get('tNumber')

       # return HttpResponse("SERVER: "+ tracking_number)
        try:
            #order = list(Order.objects.get(order_id=tracking_number))
            #db_order_json = ast.literal_eval(serializers.serialize('json', order))
            order = Order.objects.get(order_id=tracking_number)
            data = {}
            data['order_id'] = order.order_id
            data['first_name'] = order.first_name
            data['last_name'] = order.last_name
            data['address'] = order.address
            data['city'] = order.city
            data['state'] = order.state
            data['store_locatison'] = order.location
            data['price'] = order.price_total
            data['timestamp'] = str(order.timestamp)
            data['zipcode'] = order.zipcode
            data['state'] = order.state
            data['email'] = order.email
            json_data = json.dumps(data)
            jsonTemp = json_data
           # pdb.set_trace()
            return HttpResponse(json_data)
        except Order.DoesNotExist:
            raise Http404("Order does not exist")

