from django.shortcuts import get_object_or_404, render, redirect
from .models import Listing
from .models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import ListingForm


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
    category = request.GET.get('category')

    categories = Category.objects.all()
    

    if category == None:
        listings = Listing.objects.order_by('-posted_date').filter(is_published=True)

    else:
        listings = Listing.objects.filter(category__name=category, is_published=True)
    context = {
        'categories': categories,
    }
  
    return render(request, 'listings/category.html', context)

def add_listings(request):
    listings = Listing.objects.all()

    context = {}
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            category = form.cleaned_data.get("category")
            email = form.cleaned_data.get("email")
            description = form.cleaned_data.get("description")
            facebook = form.cleaned_data.get("facebook")
            instagram = form.cleaned_data.get("instagram")
            website = form.cleaned_data.get("website")
            photo_main = form.cleaned_data.get("photo_main")
            photo_1 = form.cleaned_data.get("photo_1")
            photo_2 = form.cleaned_data.get("photo_2")
            photo_3 = form.cleaned_data.get("photo_3")
            photo_4 = form.cleaned_data.get("photo_4")
            location = form.cleaned_data.get("location")
            phone_number = form.cleaned_data.get("phone_number")
            opening_time = form.cleaned_data.get("opening_time")
            closing_time = form.cleaned_data.get("closing_time")
            user_id = form.cleaned_data.get('user_id')

            #check if user have added listing before

            if request.user.is_authenticated:
                user_id = request.user.id
                has_added = Listing.objects.all().filter(user_id=user_id)
                if has_added:
                    messages.error(request, 'Your already added a listing')
                    return redirect('add_listing')

            obj = Listing.objects.create(
                                 name = name,
                                 category =category,
                                 email = email,
                                 description = description,
                                 facebook = facebook,
                                 instagram = instagram,
                                 website = website,
                                 photo_main = photo_main,
                                 photo_1 = photo_1,
                                 photo_2 = photo_2,
                                 photo_3 = photo_3,
                                 photo_4 = photo_4,
                                 location = location,
                                 phone_number = phone_number,
                                 opening_time = opening_time,
                                 closing_time = closing_time,
                                 user_id = user_id
                                 )
            obj.save()
            print(obj)
            messages.success(request, 'your listing has been successfully added, and would be under 24hours review')
    else:
        form = ListingForm()
    context = {
        'form': form,
        'listings': listings,
    }
      
    return render(request, 'listings/add_listings.html', context)