# tiles/forms.py
from django import forms
from .models import Tile

class TileForm(forms.ModelForm):
    class Meta:
        model = Tile
        fields = ['product_name', 'product_quantity', 'dealer_name']
