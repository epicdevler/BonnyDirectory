from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.Login , name="login"),
    path('register/' , views.Register , name="register"),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('logout/' , views.Logout , name="logout"),
    path('add_listing/', views.add_listing, name='add_listing'),
    path('dashboard/', views.dashboard, name='dashboard'),
]