from django.contrib import admin
from.models import Destination,Testimony,Video,Image


# Register your models here.
admin.site.register(Destination) # which means we register our class here
admin.site.register(Testimony) 


admin.site.register(Video)
admin.site.register(Image)