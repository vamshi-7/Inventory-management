from django.db import models

# Create your models here.
class Tile(models.Model):
    product_name = models.CharField(max_length=255)
    product_quantity = models.PositiveIntegerField()
    dealer_name = models.CharField(max_length=255)

    def __str__(self): # String representation of the model
        return self.product_name
    

class CustomerPurchase(models.Model):

    customer_name = models.CharField(max_length=255)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    tile_quantity = models.PositiveBigIntegerField()