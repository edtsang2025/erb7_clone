from django.urls import path
from . import views

app_name = 'hotel_listings'

urlpatterns = [
    path('', views.hotel_listings, name='hotel_listings'),
    path('hotel_listing', views.hotel_listing, name='hotel_listing'),    
#    path('<int:hotel_listing_id>', views.hotel_listing, name='hotel_listing'),
#    path('search', views.search, name='search'),
]