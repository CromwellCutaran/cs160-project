
from django.db import models

# Create your models here.

class Order(models.Model):
    SC = 'Santa Clara'
    SM = 'San Mateo'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    order_id = models.AutoField(primary_key=True, editable=False)
    price_total = models.DecimalField(max_digits=6, decimal_places=2, default="1.00")
    timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField()
    state = models.CharField(max_length=100, default="CA")
    location_choice = (
        (SC, 'Santa Clara'),
        (SM, 'San Mateo'),
    )
    location = models.CharField(max_length=2, choices=location_choice, default=SC)

    def __int__(self):
        return self.order_id

class OrderItems(models.Model):
    order_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()

    def __int__(self):
        return self.order_id

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in OrderItems._meta.fields]
