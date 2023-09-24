from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from .forms import SignupForm
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the user
            username = form.cleaned_data['username']  
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')  
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


      
def login(request):
    if request.method=="POST":
            username = request.POST["username"]
            password = request.POST["pass1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('loginhome')
        
            else:
                 messages.error(request,"There is some error in Logging in !!! Please try again")
                 return redirect('login')
    else:
             return render(request, 'login.html')
def loginhome(request):
    return render(request, 'loginhome.html')