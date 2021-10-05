from django.shortcuts import render, redirect
from django.views import View
import json
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .utils import account_activation_token
from .helpers import send_forget_password_mail
from django.urls import reverse
from django.contrib import auth
import uuid
from listings.models import Listing

# Create your views here.


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email in use, choose another one '}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry username in use, choose another one '}, status=409)
        return JsonResponse({'username_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        # GET USER DATA
        # VALIDATE
        # create a user account

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'accounts/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }

                link = reverse('activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})

                email_subject = 'Activate your account'

                activate_url = 'http://'+current_site.domain+link

                email = EmailMessage(
                    email_subject,
                    'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
                    'noreply@bonnydirect.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account successfully created, please check your mail for activation')
                return render(request, 'accounts/register.html')

        return render(request, 'accounts/register.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('index')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'accounts/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'accounts/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'accounts/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')
    

class dashboardView(View):
    listings = Listing.objects.filter(is_published=True)
    context = {
            'listings':listings
        }
    def get(self, request):
        return render(request, 'accounts/dashboard.html', context)
    
    def post(self, request):
        
        return render(request, 'accounts/dashboard.html', context)


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'accounts/forget-password.html')
    
    def post(self, request):
        try:
            if request.method == 'POST':
                username = request.POST.get('username')
            
                if not User.objects.filter(username=username).first():
                    messages.error(request, 'Not user found with this username.')
                    return redirect('forgotPassword')
            
                user_obj = User.objects.get(username = username)
                token = str(uuid.uuid4())
                profile_obj= Profile.objects.get(user = user_obj)
                profile_obj.forget_password_token = token
                profile_obj.save()
                send_forget_password_mail(user_obj.email , token)
                messages.success(request, 'An email is sent.')
            return redirect('forgotPassword')
                
    
    
        except Exception as e:
            print(e)
        return render(request, 'accounts/forget-password.html')
    
class ChangePasswordView(View):
    def get(self, request):
        return render(request, 'accounts/change-password.html')
    
    def post(self, request):
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
                    return redirect(f'changePassword/{token}/')
                
            
                if  new_password != confirm_password:
                    messages.error(request, 'Password did not match.')
                    return redirect(f'changePassword/{token}/')
                         
            
                user_obj = User.objects.get(id = user_id)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request, 'Password reset successful.')
                return redirect('login')
            
            
        
        except Exception as e:
            print(e)
        return render(request, 'accounts/change-password.html', context)