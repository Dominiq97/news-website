from django.shortcuts import render, redirect
from .models import Category

# Create your views here.

def category_list(request):
    category = Category.objects.all()
    return render(request,'back/category_list.html',{'category':category})