from django.shortcuts import render, get_object_or_404, redirect
from .models import Main 

# Create your views here.

def home(request):
 #   site_name = "News of Tech | HOME"
    site = Main.objects.get(pk=2)
    return render(request, 'front/home.html',{'sitename':site})

def about(request):
    site_name = "News of Tech | ABOUT"
    return render(request, 'front/about.html',{'sitename':site_name})