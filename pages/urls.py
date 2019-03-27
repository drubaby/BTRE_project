from django.urls import path

from . import views

urlpatterns = [
    # route, method, name of path
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
 
