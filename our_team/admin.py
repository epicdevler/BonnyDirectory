from django.contrib import admin

from .models import Team_Mate

class Team_MateAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_published')
    list_display_links = ('name', 'position',)
    list_filter = ('name', 'position',)
    search_fields = ('name', 'position',)
    list_editable = ('is_published',)



admin.site.register(Team_Mate, Team_MateAdmin)