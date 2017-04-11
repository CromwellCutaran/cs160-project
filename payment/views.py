from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order, OrderItems
#from store.models import SC_produce, SM_produce

@csrf_exempt
def payment_done(request):
    order_idm = request.session.get("order_id")
    order = Order.objects.get(order_id=order_idm)
    order.paid = True
    order.save()

    return render(request, 'payment/done.html')



@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


# Create your views here.
def payment_process(request):
    order_idm = request.session.get("order_id")
    host = request.get_host()
    order = Order.objects.get(order_id=order_idm)
    print(order.price_total)
    print(order.order_id)
    print(order)


    orderitems = OrderItems.objects.all()
    productsSM = SM_produce.objects.all()
    productsSC = SC_produce.objects.all()
    orderitemQuery = list(orderitems.filter(order_id=order_idm))
    products = []
    for item in orderitemQuery:
        product = productsSC.filter(id = item.item_id)
        products.extend(product)
    #print(orderitemQuery)
    #for x in orderitemQuery:
    #    print(x.quantity)
    #print(productsSC)
    print(products)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.price_total,
        'currency_code': 'USD',
        'invoice': str(order.order_id),
        'handling': '5.00',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),

    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'orderitemQuery': orderitemQuery, 'products': products, 'form': form, 'order': order})
