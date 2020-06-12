from django.shortcuts import render, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage

# Create your views here.

def news_detail(request,pk):
    site = Main.objects.get(pk=2)
    news = News.objects.filter(pk=pk)
    return render(request, 'front/news_detail.html',{'site':site,'news':news})

def news_list(request):
    news = News.objects.all()
    return render(request, 'back/news_list.html',{'news':news})

def news_add(request):
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newssummary = request.POST.get('newssummary')
        newsbody = request.POST.get('newsbody')
#       print(newstitle," ",newscategory," ",newssummary," ",newsbody)
        if newstitle == "" or newssummary == "" or newsbody == "" or newscategory == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})

        try:    
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                if (myfile.size < 5000000):

                    news_added = News(name=newstitle, 
                summary=newssummary, 
                body=newsbody, 
                date="2020/2/2", 
                picname=filename,
                picurl=url, 
                writer="-",
                category=newscategory,
                category_id=0,
                show=0
                )
                    news_added.save()
                    return redirect('news_list')
                else:
                    error: "Your file is bigger than 5 Mb"
                    return render(request,'back/error.html',{'error':error})
            
            else:
                error = "Your file not supported"
                return render(request,'back/error.html',{'error':error})

        except:
            error = "Please input your image"
            return render(request,'back/error.html',{'error':error})

    return render(request, 'back/news_add.html')


