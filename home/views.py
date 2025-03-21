from django.http import HttpResponse
from django.shortcuts import render
from packages.models import TravelPackage

def index(request):
    
    travel_packages =  TravelPackage.objects.all()
    ratings_range = range(1, 6)  # Range for star rating
    return render(request, 'index.html', {'packages': travel_packages, 'ratings_range': ratings_range})  # Path to your template


def not_found(request, exception=None):
    """
    Renders a 404 error page when a requested resource is not found.

    This view handles the case when a user tries to access a non-existent page and provides a custom 404 error page.
    """
    return render(request, '404.html', status=404)

