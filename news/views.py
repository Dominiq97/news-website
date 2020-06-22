from django.shortcuts import render, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime 
from subcategory.models import SubCategory
from category.models import Category

# Create your views here.

def news_detail(request,pk):
    site = Main.objects.get(pk=2)
    news = News.objects.filter(pk=pk)
    return render(request, 'front/news_detail.html',{'site':site,'news':news})

def news_list(request):
    news = News.objects.all()
    return render(request, 'back/news_list.html',{'news':news})

def news_add(request):

    now = datetime.datetime.now()
    year =  now.year
    day = now.day
    month = now.month
    if len(str(day)) == 1:
        day = "0"+str(day)
    if len(str(month)) == 1:
        month = "0"+str(month)
    today = str(year) + "/" + str(month) + "/" + str(day)

    hour = now.hour
    minute = now.minute
    if len(str(hour)) == 1:
        hour = "0"+str(hour)
    if len(str(minute)) == 1:
        minute = "0"+str(minute)

    time = str(hour) + ":" + str(minute)

    category = SubCategory.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newssummary = request.POST.get('newssummary')
        newsbody = request.POST.get('newsbody')
        newsid = request.POST.get('newscategory')
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
                    newsname=SubCategory.objects.get(pk=newsid).name
                    news_added = News(name=newstitle, 
                summary=newssummary, 
                body=newsbody, 
                date=today, 
                time=time,
                picname=filename,
                picurl=url, 
                writer="-",
                category=newsname,
                category_id=newsid,
                show=0
                )
                    news_added.save()
                    return redirect('news_list')
                else:
                    error: "Your file is bigger than 5 Mb"
                    return render(request,'back/error.html',{'error':error})
            
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "Your file not supported"
                return render(request,'back/error.html',{'error':error})

        except:
            error = "Please input your image"
            return render(request,'back/error.html',{'error':error})

    return render(request, 'back/news_add.html',{'category':category})

def news_delete(request,pk):

    try:

        news_deleted = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(news_deleted.picname)
        news_deleted.delete()
    except:
        error = "Something Wrong"
        return render(request,'back/error.html',{'error':error})


    return redirect('news_list')

def news_edit(request,pk):

    if len(News.objects.filter(pk=pk))==0:
        error = "News does not exist!"
        return render(request,'back/error.html',{'error':error})

    news = News.objects.get(pk=pk)
    category = SubCategory.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newssummary = request.POST.get('newssummary')
        newsbody = request.POST.get('newsbody')
        newsid = request.POST.get('newscategory')
        if newstitle == "" or newssummary == "" or newsbody == "" or newscategory == "":
            error = "All fields required"
            return render(request,'back/error.html',{'error':error})
        try:
            try:    
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                url = fs.url(filename)

                if str(myfile.content_type).startswith("image"):

                    if (myfile.size < 5000000):
                        newsname=SubCategory.objects.get(pk=newsid).name
                        news_edited = News.objects.get(pk=pk)

                        fss = FileSystemStorage()
                        fss.delete(news_edited.picname)

                        news_edited.name=newstitle
                        news_edited.summary=newssummary
                        news_edited.body = newsbody
                        news_edited.picname=filename
                        news_edited.picurl=url
                        news_edited.writer="-"
                        news_edited.category=newsname
                        news_edited.category_id=newsid
                        news_edited.save()
                        return redirect('news_list')
                    else:
                        fs = FileSystemStorage()
                        fs.delete(filename)
                        error: "Your file is bigger than 5 Mb"
                        return render(request,'back/error.html',{'error':error})
                
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your file not supported"
                    return render(request,'back/error.html',{'error':error})

            except:
                newsname=SubCategory.objects.get(pk=newsid).name
                news_edited = News.objects.get(pk=pk)

                news_edited.name=newstitle
                news_edited.summary=newssummary
                news_edited.body = newsbody
                news_edited.category=newsname
                news_edited.category_id=newsid

                news_edited.save()
                return redirect('news_list')
        except:
            error = "Subcategory doesn't exist"
            return render(request,'back/error.html',{'error':error})
    return render(request, 'back/news_edit.html',{'pk':pk,'news':news,'category':category})
