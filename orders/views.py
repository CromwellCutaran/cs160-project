from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
import jsonpickle
from orders.models import Order
from .models import OrderItems
from .forms import OrderForm
from store.models import SC_produce, SM_produce

def orders(request):
    store = request.session.get('store')
    cart = request.session.get('cart')

    item = []
    itemQuantity = []
    itemPrice = []
    for key, value in cart.items():
        item.append(value[0]['name'])
        itemPrice.append(round(float(value[0]['price']) * value[1], 2))
        itemQuantity.append(value[1])
    itemID = []
    if store == 'SC':
        for items in item:
            itemID.append(SC_produce.objects.get(name=items).id)
    else:
        for items in item:
            itemID.append(SM_produce.objects.get(name=items).id)
    combined = zip(item, itemQuantity, itemPrice, itemID)
    total = 0
    for prices in itemPrice:
        total += prices
    roundedTotal = round(total, 2)
    li_result = list(combined)
    result = jsonpickle.encode(li_result)
    request.session['result'] = result
    print(store)

    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        orderObject = Order.objects.get(order_id=instance.order_id)
        orderObject.price_total = total
        if store == 'sc':
            orderObject.location = Order.SC
        else:
            orderObject.location = Order.SM

        orderObject.save()
        request.session['order_id'] = instance.order_id


        for item, quan, price, id in li_result:
            OrderItems.objects.create(order_id=instance.order_id, item_id=id, quantity=quan)

        return HttpResponseRedirect(reverse('payment:process'))

    #if request.method == "POST":
    #    print(request.POST.get("first_name"))
    context = {
        "form": form,
    }

    return render(request, "orders/orders.html", {'myform': form, 'li_result':li_result, "roundedTotal": roundedTotal})