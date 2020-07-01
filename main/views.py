from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from category.models import Category

# Create your views here.

def home(request):
 #   site_name = "News of Tech | HOME"
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    category = Category.objects.all()
    return render(request, 'front/home.html',{'site':site,'news':news,'category':category})

def about(request):
    site = Main.objects.get(pk=2)
    return render(request, 'front/about.html',{'site':site})


def panel(request):
    return render(request,'back/home.html')