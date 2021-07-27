from django.shortcuts import get_object_or_404, render
from .models import Listing
from .models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.models import Category


def index(request):
    listings = Listing.objects.order_by('-posted_date').filter(is_published=True)

    category = request.GET.get('category')

    categories = Category.objects.all()
    

    if category == None:
        listings = Listing.objects.order_by('-posted_date').filter(is_published=True)

    else:
        listings = Listing.objects.filter(category__name=category, is_published=True)
        
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
    'listings': paged_listings,
    'categories': categories,
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)


    context = {
        'listing': listing,
    }
  
    return render(request, 'listings/listing.html', context) 

def search(request):
    queryset_list = Listing.objects.order_by('-posted_date').filter(is_published=True)
    category = request.GET.get('category')
    categories = Category.objects.all()

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
  
    #location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(location__icontains=location)
    
    #search by category
    if 'category' in category:
        category = request.Get['category']
    elif category:
        queryset_list = Listing.objects.filter(category__name=category, is_published=True)
        
    context ={
        'listings': queryset_list,
        'categories': categories,
    }

    return render(request, 'listings/search.html', context)

def category(request):
    categories = Category.objects.all()


    context = {
        'categories': categories,
    }
  
    return render(request, 'listings/category.html', context) 
