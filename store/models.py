from django.db import models

# represents a typical product in OFS
class SM_produce(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    # arguments of model type means
    #  an item can be up to $99.99
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # using CharField for now
    #  use FilePathField instead ?
    image_path = models.CharField(max_length=5000)
    category = models.CharField(max_length=100)
    amount_left = models.IntegerField()

class SC_produce(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    # arguments of model type means
    #  an item can be up to $99.99
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # using CharField for now
    #  use FilePathField instead ?
    image_path = models.CharField(max_length=5000)
    category = models.CharField(max_length=100)
    amount_left = models.IntegerField()
