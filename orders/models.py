import uuid

from django.db import models

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    order_id = models.AutoField(primary_key=True, editable=False)
    price_total = models.DecimalField(max_digits=6, decimal_places=2, default="95.00")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.order_id
