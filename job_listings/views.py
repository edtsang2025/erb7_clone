from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, Paginator

# Create your views here.

from job_listings.models import Job_Listing


def job_listings(request):

    job_listings = Job_Listing.objects.filter(is_published=True)

    paginator = Paginator(job_listings,5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {"job_listings":paged_listings,}

    return render(request, 'job_listings/job_listings.html', context)


def job_listing(request, job_listing_id):

    job_listing = get_object_or_404(Job_Listing, pk=job_listing_id)
    context = {"job_listing":job_listing,}

    return render(request, 'job_listings/job_listing.html', context)


