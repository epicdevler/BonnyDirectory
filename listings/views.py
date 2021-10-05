from django.shortcuts import get_object_or_404, render, redirect
from .models import Listing
from .models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

# @login_required(login_url='/accounts/login')
def add_listings(request):
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']
        category = request.POST['category']
        location = request.POST['location']
        phone_number = request.POST['phone_number']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        website = request.POST['website']
        photo_main = request.POST['photo_main']
        photo_1 = request.POST['photo_1']
        photo_2 = request.POST['photo_2']
        photo_3 = request.POST['photo_3']
        photo_4 = request.POST['photo_4']
        opening_time = request.POST['opening_time']
        closing_time = request.POST['closing_time']
        user_id = request.POST['user_id']
        
        #verifying form / user details
        
        if not name:
            messages.error(request, 'Business name is required.')
            return redirect('add_listings')
        
        if not phone_number:
            messages.error(request, 'Business number is required.')
            return redirect('add_listings')
        
        if not email:
            messages.error(request, 'Business email is required.')
            return redirect('add_listings')
        
        if not category:
            messages.error(request, 'Business category is required.')
            return redirect('add_listings')
        
        if not location:
            messages.error(request, 'Business location is required.')
            return redirect('add_listings')
        
        if not photo_main:
            messages.error(request, 'Business main image is required.')
            return redirect('add_listings')
        
        if not description:
            messages.error(request, 'Business description is required.')
            return redirect('add_listings')
        
        add = Listing(name=name, email=email, category=category, description=description, location=location, phone_number=phone_number, 
                      facebook=facebook, instagram=instagram, website=website, photo_main=photo_main, photo_1=photo_1, photo_2=photo_2, 
                      photo_3=photo_3, photo_4=photo_4)
        add.save()
        messages.success(request, "Your Business has been added successfully, under a 24hour review.")
    return render(request, 'listings/add_listings.html', context)

def edit_listing(request, id):
    listings = Listing.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'listings': listings,
        'values': listings,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, 'istings/edit_listing.html', context)
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            description = request.POST['description']
            category = request.POST['category']
            location = request.POST['location']
            phone_number = request.POST['phone_number']
            facebook = request.POST['facebook']
            instagram = request.POST['instagram']
            website = request.POST['website']
            photo_main = request.POST['photo_main']
            photo_1 = request.POST['photo_1']
            photo_2 = request.POST['photo_2']
            photo_3 = request.POST['photo_3']
            photo_4 = request.POST['photo_4']
            opening_time = request.POST['opening_time']
            closing_time = request.POST['closing_time']
            user_id = request.POST['user_id']
        
        
        
            if not name:
                messages.error(request, 'Business name is required.')
                return redirect('add_listings')
        
            if not phone_number:
                messages.error(request, 'Business number is required.')
                return redirect('add_listings')
        
            if not email:
                messages.error(request, 'Business email is required.')
                return redirect('add_listings')
        
            if not category:
                messages.error(request, 'Business category is required.')
                return redirect('add_listings')
        
            if not location:
                messages.error(request, 'Business location is required.')
                return redirect('add_listings')
        
            if not photo_main:
                messages.error(request, 'Business main image is required.')
                return redirect('add_listings')
        
            if not description:
                messages.error(request, 'Business description is required.')
                return redirect('add_listings')

            listings.user_id = request.user
            listings.name = request.name
            listings.email = request.email
            listings.category = request.category
            listings.location = request.location
            listings.photo_main = request.photo_main
            listings.photo_1 = request.photo_1
            listings.photo_2 = request.photo_2
            listings.photo_3 = request.photo_3
            listings.photo_4 = request.photo_4
            listings.description = request.description
            listings.phone_number = request.phone_number
            listings.closing_time = request.closing_time
            listings.opening_time = request.opening_time
            listings.website = request.website
            listings.facebook = request.facebook

            listings.save()
            messages.success(request, 'Listing updated  successfully')

        return redirect('dashboard')
    
def delete_listing(request, id):
    listings = Listings.objects.get(pk=id)
    listings.delete()
    messages.success(request, 'Listing removed')
    return redirect('dashboard')