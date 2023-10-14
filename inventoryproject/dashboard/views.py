from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TileForm, CustomerPurchaseForm
from .models import Tile, CustomerPurchase

# Create your views here.
def index(request):
    return render(request, "home.html")


def staff(request):
    return HttpResponse('This is the staff page..!!')


def add_tile(request):
    if request.method == 'POST':
        form = TileForm(request.POST)
        if form.is_valid():
            form.save()
            #print(form.cleaned_data['product_name'])
            #print(form.cleaned_data['product_quantity'])
            #print(form.cleaned_data['dealer_name'])
            return HttpResponse("Successfully added data..!!")  # Redirect to a page showing all tiles
    else:
        form = TileForm()
    return render(request, 'tile_form.html', {'form': form})


def tile_list(request):
    tiles = Tile.objects.all()  # Retrieve all tiles from the database
    return render(request, 'tile_list.html', {'tiles': tiles})


def customer_purchase(request):
    if request.method == 'POST':
        form = CustomerPurchaseForm(request.POST)
        if form.is_valid():
            customer_purchase = form.save()

            #Update the tile quantity
            tile = customer_purchase.tile
            tile.product_quantity -= customer_purchase.tile_quantity
            tile.save()

            return HttpResponse("Successfully added data...!!")
    else:
        form = CustomerPurchaseForm()
    
    context = {'form': form}
    return render(request, 'customer_purchase.html', context)


def customer_purchase_list(request):
    customer_purchases = CustomerPurchase.objects.all()
    return render(request, 'customerpurchase_list.html',
                   {'customer_purchases': customer_purchases})