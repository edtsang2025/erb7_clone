from django.shortcuts import render, get_object_or_404
#from .models import HotelListing
from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q

# Create your views here.

def hotel_listings(request):
    return render(request, 'hotel_listings/hotel_listings.html')

def hotel_listing(request):
    return render(request, 'hotel_listings/hotel_listing.html')

