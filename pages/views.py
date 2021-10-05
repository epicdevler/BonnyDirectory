from django.shortcuts import render
from listings.models import Listing
from listings.models import Category
from our_team.models import Team_Mate
from testimony.models import Testimony
from news_tips.models import NewsPost
from django.db.models import Count






def index(request):
    listings = Listing.objects.order_by('-posted_date').filter(is_published=True)[:8]
    testimonies = Testimony.objects.all()[:3]
    news = NewsPost.objects.all()[:3]
    
    # category = Category.objects.all().annotate(cate_count= Count('name'))[:6]
    category = Category.objects.all()[:9]
    search_category = Category.objects.all()[:5]
    
    context = {
        'listings': listings,
        'testimonies': testimonies,
        'categories': category,
        'search_category': search_category,
        'news':news,
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
