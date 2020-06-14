from django.shortcuts import render, redirect
from .models import Category

# Create your views here.

def category_list(request):
    category = Category.objects.all()
    return render(request,'back/category_list.html',{'category':category})

def category_add(request):
    if request.method =='POST':
        catname=request.POST.get('catname')
        if catname == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})
        if len(Category.objects.filter(name=catname)) != 0 :
            error = "This Name Used Before!"
            return render(request,'back/error.html',{'error':error})
        category = Category(name=catname)
        category.save()
        return redirect('category_list')


    return render(request,'back/category_add.html')