from django.contrib import admin
from .models import Listing
from .models import Category


class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published', 'location', 'email', 'user_id')
    list_display_links = ('name', 'category')
    list_filter = ('category', 'location')
    list_editable = ('is_published',)
    search_fields = ('name', 'category', 'location', 'user_id')


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category)