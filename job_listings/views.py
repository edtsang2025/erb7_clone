from django.shortcuts import render

# Create your views here.

def job_listings(request):
    return render(request, 'job_listings/job_listings.html')

def job_listing(request):
    return render(request, 'job_listings/job_listing.html')