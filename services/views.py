from django.shortcuts import render
from .models import Bookings
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from plumbing.models import Testimony,Video,Image


# Create your views here.
def service(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        select_service = request.POST['select_service']
        date = request.POST['date'] 
        special_request = request.POST['special_request']
        phonenumber = request.POST['phonenumber']
        
       #ssave booking services information
        bookings = Bookings.objects.create(
           name = name,
           email = email,
           select_service = select_service,
           date = date,
           special_request = special_request,
           phonenumber = phonenumber,
       )
    else:
        messages.success(request,"was added successfully. You may add another bookings below..")
    return render(request,'service.html')
    
        

 
def fourzerofoure(request):

    context = {
        'plumbing_images': Image.objects.filter(category='plumbing'),
        'tree_images': Image.objects.filter(category='tree'),
        'plumbing_videos': Video.objects.filter(category='plumbing'),
        'tree_videos': Video.objects.filter(category='tree'),
    }

    return render(request,'images.html',context)    

def booking(request):
    return render(request,'booking.html')
    
def testmony(request):
    testmoni = Testimony.objects.all()#this is only a way to fetch data from the database
    # for the picture to appear go to index.py
    return render(request,'testimonial.html',{'testmoni':testmoni})

  



def contact(request):
    if request.method == 'POST':
        names = request.POST['names']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
       #ssave booking services information
        send_message = Contact.objects.create(
           names = names,
           email = email,
           subject = subject,
           message = message,
       )
    else:
        messages.success(request,"message successfully send ....")
    return render(request,'contact.html')



