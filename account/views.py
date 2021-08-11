from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages, auth
from listings.models import Listing
from listings.models import Category
from .forms import ListingForm
from .helpers import send_forget_password_mail
from django.core.mail import EmailMessage


def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                messages.error(request, 'Both Username and Password are required.')
                return redirect('login')
            user_obj = User.objects.filter(username=username).first()
            if user_obj is None:
                messages.error(request, 'User not found.')
                return redirect('login')
        
        
            user = authenticate(username = username , password = password)
            
            if user is None:
                messages.error(request, 'Wrong password.')
                return redirect('login')
        
            login(request , user)
            return redirect('index')

                
            
            
    except Exception as e:
        print(e)
    return render(request , 'accounts/login.html')



def Register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            c_password = request.POST.get('c_password')
            
            if password == c_password:
                try:
                    if User.objects.filter(username = username).first():
                        messages.error(request, 'Username is taken.')
                        return redirect('register')
                      
                    if User.objects.filter(email = email).first():
                        messages.error(request, 'Email is taken.')
                        return redirect('register')
                    
                    if len(password) < 6:
                        message.error(request, 'password too short')
                        return redirect('register')
                
                    
                    user_obj = User(username=username, email=email, password=password)
                    user_obj.set_password(password)
                    user_obj.save()
                        
                    profile_obj = Profile.objects.create(user = user_obj)
                    profile_obj.save()

                    return redirect('login')
                    
            
                except Exception as e:
                    print(e)
            else:
                messages.error(request, 'password did not match.')
                return redirect('register')
       
    except Exception as e:
            print(e)

    return render(request , 'accounts/register.html')


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')



def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.error(request, 'No user id found.')
                return redirect(f'change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.error(request, 'Password did not match.')
                return redirect(f'change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, 'Password reset successful.')
            return redirect('login')
            
            
            
    except Exception as e:
        print(e)
    return render(request , 'accounts/change-password.html' , context)


import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            
            if not User.objects.filter(email=email).first():
                messages.error(request, 'Not user found with this email.')
                return redirect('forget-password')
            
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('forget-password')
    
    
    except Exception as e:
        print(e)
    return render(request , 'accounts/forget-password.html')

    
def dashboard(request):
    listings = Listing.objects.all()

    context = {
    'listings': listings,
    }

    if request.user.is_authenticated:
        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('login')



# def add_listing(request):
#     listings = Listing.objects.all()

#     context = {}
#     if request.method == "POST":
#         form = ListingForm(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             category = form.cleaned_data.get("category")
#             email = form.cleaned_data.get("email")
#             description = form.cleaned_data.get("description")
#             facebook = form.cleaned_data.get("facebook")
#             instagram = form.cleaned_data.get("instagram")
#             website = form.cleaned_data.get("website")
#             photo_main = form.cleaned_data.get("photo_main")
#             photo_1 = form.cleaned_data.get("photo_1")
#             photo_2 = form.cleaned_data.get("photo_2")
#             photo_3 = form.cleaned_data.get("photo_3")
#             photo_4 = form.cleaned_data.get("photo_4")
#             location = form.cleaned_data.get("location")
#             phone_number = form.cleaned_data.get("phone_number")
#             opening_time = form.cleaned_data.get("opening_time")
#             closing_time = form.cleaned_data.get("closing_time")
#             user_id = form.cleaned_data.get('user_id')

#             # check if user have added listing before

#             # if request.user.is_authenticated:
#             #     user_id = request.user.id
#             #     has_added = Listing.objects.all().filter(user_id=user_id)
#             #     if has_added:
#             #         messages.error(request, 'Your already added a listing')
#             #         return redirect('add_listing')

#             obj = Listing.objects.create(
#                                 name = name,
#                                 category =category,
#                                 email = email,
#                                 description = description,
#                                 facebook = facebook,
#                                 instagram = instagram,
#                                 website = website,
#                                 photo_main = photo_main,
#                                 photo_1 = photo_1,
#                                 photo_2 = photo_2,
#                                 photo_3 = photo_3,
#                                 photo_4 = photo_4,
#                                 location = location,
#                                 phone_number = phone_number,
#                                 opening_time = opening_time,
#                                 closing_time = closing_time,
#                                 user_id = user_id
#                              )
#             obj.save()
#             print(obj)
#             messages.success(request, 'your listing has been successfully added, and would be under 24hours review')
#     else:
#         form = ListingForm()
#     context = {
#         'form': form,
#         'listings': listings,
#     }
      
#     return render(request, 'accounts/add_listing.html', context)

