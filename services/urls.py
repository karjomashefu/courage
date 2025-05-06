from django.urls import path
from . import views

urlpatterns = [
    path("service",views.service,name='service'),
    path("bookings",views.booking,name='booking'),
    path("testmony",views.testmony,name='testmony'),
    path("contact",views.contact,name='contact'),
    path("404",views.fourzerofoure,name='404'),

]
