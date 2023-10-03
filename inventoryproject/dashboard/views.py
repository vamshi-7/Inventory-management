from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TileForm
from .models import Tile

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
            print(form.cleaned_data['product_name'])
            print(form.cleaned_data['product_quantity'])
            print(form.cleaned_data['dealer_name'])
            return HttpResponse("Successfully added data..!!")  # Redirect to a page showing all tiles
    else:
        form = TileForm()
    return render(request, 'tile_form.html', {'form': form})


def tile_list(request):
    tiles = Tile.objects.all()  # Retrieve all tiles from the database
    return render(request, 'tile_list.html', {'tiles': tiles})

