from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["order_id", "first_name", "last_name"]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)