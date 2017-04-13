from django.db import models
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from orders.models import Order

# Create your models here.
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != 'cs160.business@gmail.com':
            return
        if ipn_obj.receiver_email == 'cs160.business@gmail.com':
            order = Order.objects.get(order_id=ipn_obj.custom)
            order.paid = True
            order.save()

valid_ipn_received.connect(show_me_the_money)