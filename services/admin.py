from django.contrib import admin
from.models import Bookings,Contact


# Register your models here.

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('name','email','select_service','special_request','date','phonenumber')
    search_fields = ('name','email','phonenumber')
    list_filter = ('name','email','select_service','date','phonenumber')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('names','email','subject','message')
    search_fields = ('names','email')
    list_filter = ('names','email')
