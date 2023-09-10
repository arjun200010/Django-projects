from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is home")
def about(request):
    return render(request,"about.html")
   # return HttpResponse("This is about page")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("This is service we provide")
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        
        mail=request.POST.get('mail')
       
        number=request.POST.get('number')
       
        contact=Contact(name=name,mail=mail,number=number)
      
        contact.save()
    return render(request,"contact.html")
    #return HttpResponse("This is contact page")