from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path("about",views.about,name='about'),
    path("team",views.team,name='team'),
]

