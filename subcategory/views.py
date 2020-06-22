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

def subcategory_edit(request,pk):

    if len(SubCategory.objects.filter(pk=pk))==0:
        error = "Category does not exist!"
        return render(request,'back/error.html',{'error':error})
    subcategory = SubCategory.objects.get(pk=pk)
    category = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        catname = request.POST.get('category')
        catid = request.POST.get('category')
        if name == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})
        try:
            subcategory_category = Category.objects.get(pk=catid).name
            subcategory_edited = SubCategory.objects.get(pk=pk)
            subcategory_edited.name=name
            subcategory_edited.catname=subcategory_category
            subcategory_edited.catid=catid
            subcategory_edited.save()
            return redirect('subcategory_list')
                    
        except:
            subcategory_edited = SubCategory.objects.get(pk=pk)
            subcategory_edited.name=name
            subcategory_edited.catname=catname
            subcategory_edited.catid=catid
            subcategory_edited.save()
            return redirect('subcategory_list')
    return render(request, 'back/subcategory_edit.html',{'pk':pk,'subcategory':subcategory,'category':category})