from django.contrib import admin
from .models import Listing

# Where we customize admin stuff for listings app

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    # Single params need commas
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # pagination
    list_per_page = 25
    
# Register model
admin.site.register(Listing, ListingAdmin)
