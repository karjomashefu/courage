from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1== password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username already taken')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save(); 
                messages.info(request,'account successufly  created')
                return redirect('login')
        else:
            messages.info(request,'password did not match')
            return redirect('register')
        return redirect('/')

    else:
    
        return render(request,'register.html') 
      

    #LOGIN PAGE 
       
def login(requiest):
    if requiest.method == 'POST':
        username = requiest.POST['username']
        password = requiest.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(requiest,user)
            return redirect('/')
        
        else:
            messages.info(requiest,'invalid cresdentials')
            return redirect('login')
    else:
        return render(requiest,'login.html')
        

def logout(request):
    auth.logout(request)
    return redirect('/')

