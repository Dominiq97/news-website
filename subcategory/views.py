from django.shortcuts import render, redirect
from .models import SubCategory
from category.models import Category
# Create your views here.

def subcategory_list(request):
    subcategory = SubCategory.objects.all()
    return render(request,'back/subcategory_list.html',{'subcategory':subcategory})

def subcategory_add(request):
    category = Category.objects.all()
    if request.method =='POST':
        name = request.POST.get('subcatname')
        catid=request.POST.get('category')
        if name == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})
        if len(SubCategory.objects.filter(name=name)) != 0 :
            error = "This Name Used Before!"
            return render(request,'back/error.html',{'error':error})
        catname = Category.objects.get(pk=catid).name
        subcat = SubCategory(name=name,catname=catname,catid=catid)
        subcat.save()
        return redirect('subcategory_list')


    return render(request,'back/subcategory_add.html',{'category':category})


def subcategory_delete(request,pk):
    try:
        subcat_deleted = SubCategory.objects.get(pk=pk)
        subcat_deleted.delete()
    except:
        error = "Something Wrong"
        return render(request,'back/error.html',{'error':error})
    return redirect('subcategory_list')