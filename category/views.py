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

def category_delete(request,pk):

    try:
        category_deleted = Category.objects.get(pk=pk)
        category_deleted.delete()
    except:
        error = "Something Wrong"
        return render(request,'back/error.html',{'error':error})
    return redirect('category_list')

def category_edit(request,pk):

    if len(Category.objects.filter(pk=pk))==0:
        error = "Category does not exist!"
        return render(request,'back/error.html',{'error':error})

    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        catname = request.POST.get('catname')
        if catname == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})
        try:
            category_edited = Category.objects.get(pk=pk)
            category_edited.name=catname
            category_edited.save()
            return redirect('category_list')
                    
        except:
            category_edited = Category.objects.get(pk=pk)
            category_edited.name=catname
            category_edited.save()
            return redirect('category_list')
    return render(request, 'back/category_edit.html',{'pk':pk,'category':category})
