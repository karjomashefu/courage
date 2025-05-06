from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination,Testimony
from django.contrib import messages
 
def index(request):
    if request.method == 'POST':
        image = request.FILES['image']
        full_name = request.POST['name']
        profession = request.POST['profession']
        designation = request.POST['description']
       #save testmony  information
        testimony = Testimony.objects.create(
           image = image,
           full_name = full_name,
           profession = profession,
           designation = designation,
       )
    else:
        messages.success(request,"message successfully send ....")
    
    dests = Destination.objects.all()#this is only a way to fetch data from the database
    # for the picture to appear go to index.py
    

    return render(request,'index.html',{'dests':dests})


def about(request):
    dests = Destination.objects.all()

    return render(request,'about.html',{'dests':dests})

def team(request):
    dests = Destination.objects.all()

    return render(request,'team.html',{'dests':dests})
