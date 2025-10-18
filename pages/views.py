from django.shortcuts import render
#from django.http import HttpResponse

from listings.models import Listing
from doctors.models import Doctor
from listings.choices import district_choices, rooms_choices, room_choices

from hotel_listings.models import Hotel_Listing
from hotel_listings.choices import city_choices

# Create your views here.

# functions

# views.index

def index(request):
#    listings = Listing.objects.filter(is_published=True)[:3]
#    context = {"listings":listings,
#               "district_choices":district_choices,
#               "rooms_choices":rooms_choices,
#               "room_choices":room_choices
#               }
    
    hotel_listings = Hotel_Listing.objects.filter(is_published=True)[:3]
    context = {"hotel_listings":hotel_listings,
               "city_choices":city_choices}
    
    return render(request, 'pages/index.html', context)

# views.about

def about(request):
    hotel_listings = Hotel_Listing.objects.filter(is_published=True)[:3]
    context = {"hotel_listings":hotel_listings,
               "city_choices":city_choices}
    
    return render(request, 'pages/about.html', context)

def faqs(request):
    return render(request, 'pages/faqs.html')

# views.testing

def testing(request):
#    print(request.path)
    doctors = Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors = Doctor.objects.all().filter(is_mvp=True)
    context = {
        "doctors":doctors,
        "mvp_doctors":mvp_doctors
    }
    return render(request, 'pages/testing.html', context)

def testing2(request):
    return render(request, 'pages/testing2.html')