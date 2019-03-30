from django.contrib import admin
from .models import Listing

# Where we customize admin stuff for listings app

# Register
admin.site.register(Listing)
