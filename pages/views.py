from django.shortcuts import render

from listings.models import Listing
from listings.models import Category
from testimonies.models import Testimony
from our_team.models import Team_Mate
from testimonies.models import Testimony
from django.db.models import Count

def index(request):
    listings = Listing.objects.order_by('-posted_date').filter(is_published=True)[:8]
    
    
    categories = Category.objects.all().annotate(cate_count= Count('listing'))[:6]
    
    context = {
        'listings': listings,
        'categories': categories,
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    our_team = Team_Mate.objects.all().filter(is_published=True)
    testimonies = Testimony.objects.all().filter(is_published=True)

    context = {
        'our_team': our_team,
        'testimonies': testimonies,
    }
    
    return render(request, 'pages/about.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def terms_conditions(request):
    return render(request, 'pages/terms_conditions.html')
