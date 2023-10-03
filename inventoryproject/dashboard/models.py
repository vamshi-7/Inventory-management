from django.db import models

# Create your models here.
class Tile(models.Model):
    product_name = models.CharField(max_length=255)
    product_quantity = models.PositiveIntegerField()
    dealer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name