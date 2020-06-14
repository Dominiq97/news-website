from django.shortcuts import render, redirect
from .models import SubCategory

# Create your views here.

def subcategory_list(request):
    subcategory = SubCategory.objects.all()
    return render(request,'back/subcategory_list.html',{'subcategory':subcategory})

def subcategory_add(request):
    if request.method =='POST':
        catname=request.POST.get('catname')
        if catname == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})
        if len(SubCategory.objects.filter(name=catname)) != 0 :
            error = "This Name Used Before!"
            return render(request,'back/error.html',{'error':error})
        


    return render(request,'back/subcategory_add.html')