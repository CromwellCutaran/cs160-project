from django.shortcuts import render, get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order, OrderItems
from store.models import SC_produce, SM_produce
import jsonpickle

@csrf_exempt
def payment_done(request):
    #order_idm = request.session.get("order_id")
    #order = Order.objects.get(order_id=order_idm)
    #order.paid = True
    #order.save()

    return render(request, 'payment/done.html')



@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


# Create your views here.
def payment_process(request):
    order_idm = request.session.get("order_id")
    li_result = request.session.get("result")
    result = jsonpickle.decode(li_result)
    host = request.get_host()
    order = Order.objects.get(order_id=order_idm)


    orderitems = OrderItems.objects.all()
    productsSM = SM_produce.objects.all()
    productsSC = SC_produce.objects.all()
    orderitemQuery = list(orderitems.filter(order_id=order_idm))
    products = []
    for item in orderitemQuery:
        product = productsSC.filter(id = item.item_id)
        products.extend(product)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'custom': order.order_id,
        'amount': order.price_total,
        'item_name': str(order.order_id),
        'invoice': str(order.order_id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),

    }

    print(paypal_dict)

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'orderitemQuery': orderitemQuery, 'products': products, 'form': form,
                                                    'order': order, 'result': result})



