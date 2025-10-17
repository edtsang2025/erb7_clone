from django.urls import path
from . import views # import views.py in the same directory

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('faqs', views.faqs, name='faqs'),    
    path('testing2', views.testing2, name='testing2'),
    path('testing', views.testing, name='testing'),
]