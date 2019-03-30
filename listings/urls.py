from django.urls import path

from . import views
urlpatterns = [
    # route, method, name of path

    # empty string pertains to /listings
    path('', views.index, name='listings'),

    # parameter of listing id integer
    path('<int: listing_id>', views.listing, name='listing '),

    path('search', views.search, name='search')
]
