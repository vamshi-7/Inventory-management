from django.contrib import admin

# Register your models here.
from dashboard.models import Tile, CustomerPurchase

admin.site.register(Tile)
admin.site.register(CustomerPurchase)
