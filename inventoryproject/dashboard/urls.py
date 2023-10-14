from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('add/', views.add_tile, name='add_tile'),
    path('tile_list/', views.tile_list, name='tile_list'),
    path('customer_purchase/', views.customer_purchase,
         name='customer_purchase'),
    path('customerpurchase_list', views.customer_purchase_list,
         name="customerpurchase_list"),

]




