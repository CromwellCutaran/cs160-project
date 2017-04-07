from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

from orders.models import Order
from .forms import OrderForm


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
    return render(request, "orders/orders.html", {'myform': form})