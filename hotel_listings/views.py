from django.shortcuts import render, get_object_or_404
from .models import Hotel_Listing
from django.core.paginator import EmptyPage, Paginator
from django.db.models import Q
from hotel_listings.choices import city_choices

# Create your views here.

def hotel_listings(request):

    hotel_listings = Hotel_Listing.objects.filter(is_published=True)

    paginator = Paginator(hotel_listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {"hotel_listings":paged_listings,
               "city_choices":city_choices}

    return render(request, 'hotel_listings/hotel_listings.html', context)



def hotel_listing(request, hotel_listing_id):

#    listing = get_object_or_404(Listing, pk=listing_id)
#    context = {"listing":listing}
#   return render(request, 'listings/listing.html', context)

    hotel_listing = get_object_or_404(Hotel_Listing, pk=hotel_listing_id)
    context = {"hotel_listing":hotel_listing,
               "city_choices":city_choices
    }
    return render(request, 'hotel_listings/hotel_listing.html', context)


def hotel_search(request):
    queryset_list = Hotel_Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list =  queryset_list.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list =  queryset_list.filter(city__iexact=city)
    
    paginator = Paginator(queryset_list,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {"hotel_listings":paged_listings,
               "city_choices":city_choices,
               "values":request.GET}
    
    return render(request, 'hotel_listings/hotel_search.html', context)

