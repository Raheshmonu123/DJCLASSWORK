from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 

    path('forhome', views.forhome, name='forhome'),
    path('about', views.about, name='about'),
    
]
    
