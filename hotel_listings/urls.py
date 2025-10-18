from django.urls import path
from . import views

app_name = 'hotel_listings'

urlpatterns = [
    path('', views.hotel_listings, name='hotel_listings'),
    path('<int:hotel_listing_id>', views.hotel_listing, name='hotel_listing'),
    path('hotel_search', views.hotel_search, name='hotel_search'),
]