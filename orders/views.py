from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

from orders.models import Order
from .models import OrderItems
from .forms import OrderForm
from store.models import SC_produce, SM_produce


#def orders(request):
#    return render(request, 'orders/orders.html')

def orders(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance.order_id)
        request.session['order_id'] = instance.order_id
        return HttpResponseRedirect(reverse('payment:process'))

    #if request.method == "POST":
    #    print(request.POST.get("first_name"))
    context = {
        "form": form,
    }

    itemid1 = 1
    itemid2 = 1
    itemid3 = 1
    quan1 = 4
    quan2 = 1
    quan3 = 2

    OrderItem = OrderItems






    return render(request, "orders/orders.html", {'myform': form})