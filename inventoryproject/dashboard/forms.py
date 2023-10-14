# tiles/forms.py
from django import forms
from .models import Tile, CustomerPurchase

class TileForm(forms.ModelForm):
    class Meta:
        model = Tile
        fields = ['product_name', 'product_quantity', 'dealer_name']


class CustomerPurchaseForm(forms.ModelForm):

    class Meta:
        model = CustomerPurchase
        fields = ['customer_name', 'tile', 'tile_quantity']


