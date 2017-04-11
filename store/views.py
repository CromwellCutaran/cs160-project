from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
#from store.models import Order #creating temp model to test traking page
from .models import OrderItems
from .models import Order






def index(request):
    return render(request, 'store/index0.html')


def track(request):
    return render(request, 'store/trackingPage.html')

@require_GET
@csrf_exempt
def post_tracking(request):
    if request.method == 'GET':  #get from data base
        tracking_number = request.GET.get('tNumber')
        return HttpResponse("SERVER: "+ tracking_number)
