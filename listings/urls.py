from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search',views.search, name='search'),
    path('add_listings', views.add_listings, name='add_listings'),
    path('<int:listing_id>', views.edit_listing, name="edit_listing"),
    path('<int:listing_id>', views.delete_listing, name="delete_listing"),
    path('category',views.category, name='category'),
]