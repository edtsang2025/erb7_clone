from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
    path('article', views.article, name='article'),    
#    path('<int:hotel_listing_id>', views.hotel_listing, name='hotel_listing'),
#    path('search', views.search, name='search'),
]