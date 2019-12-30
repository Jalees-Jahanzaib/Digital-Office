from django.shortcuts import render
from .models import Files 
# Create your views here.

def home(request):
    context={
        'Files': Files.objects.all()
    }
    
    return render(request,"blog/home.html",context)

def about(request): 
    return render(request,"blog/about.html")
