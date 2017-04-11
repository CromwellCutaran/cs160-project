from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

from orders.models import Order
from .models import OrderItems
from .forms import OrderForm
#from store.models import SC_produce, SM_produce


#def orders(request):
#    return render(request, 'orders/orders.html')

def orders(request):
    #test items and test quantities
    itemid1 = 1
    itemid2 = 2
    itemid3 = 3
    quan1 = 4
    quan2 = 1
    quan3 = 2
    #request.session from cart
    productsSC = SC_produce.objects.all()
    items = [itemid1, itemid2, itemid3]
    itemquery = []
    quantity = [quan1, quan2, quan3]
    itemprices = []
    for item in items:
        itemquery.extend(productsSC.filter(id=item))
    print(itemquery)
    for item, quan in zip(itemquery,quantity):
        itemprice = item.price
        itemprices.append(itemprice * quan)
    #print(itemprices)
    combined = zip(itemquery, quantity, itemprices)
    total = 0
    for prices in itemprices:
        total += prices

    #print(total)
    li_result = list(combined)

    #print(li_result)




    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        orderObject = Order.objects.get(order_id=instance.order_id)
        orderObject.price_total = total
        orderObject.save()
        #print(instance.order_id)
        request.session['order_id'] = instance.order_id


        OrderItem1 = OrderItems.objects.create(order_id=instance.order_id, item_id=itemid1, quantity=quan1)
        OrderItem2 = OrderItems.objects.create(order_id=instance.order_id, item_id=itemid2, quantity=quan2)
        OrderItem = OrderItems.objects.create(order_id=instance.order_id, item_id=itemid3, quantity=quan3)


        return HttpResponseRedirect(reverse('payment:process'))

    #if request.method == "POST":
    #    print(request.POST.get("first_name"))
    context = {
        "form": form,
    }







    return render(request, "orders/orders.html", {'myform': form, 'li_result':li_result, "total": total})