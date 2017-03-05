from django.db import models

# represents a typical product in OFS
class Product(models.Model):
    name = models.CharField(max_length=100)
    # arguments of model type means
    #  an item can be up to $99.99
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # using CharField for now
    #  use FilePathField instead ?
    image_path = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

