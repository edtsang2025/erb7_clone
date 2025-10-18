from django.urls import path
from . import views

app_name = 'job_listings'

urlpatterns = [
    path('', views.job_listings, name='job_listings'),
    path('<int:job_listing_id>', views.job_listing, name='job_listing'),    
#    path('<int:hotel_listing_id>', views.hotel_listing, name='hotel_listing'),
#    path('search', views.search, name='search'),
]