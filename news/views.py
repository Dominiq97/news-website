import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder
from django.shortcuts import render, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime 
from subcategory.models import SubCategory
from category.models import Category
from news.forms import (SimpleForm, PostForm)
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


# Create your views here.

def news_detail(request,pk):
    site = Main.objects.get(pk=2)
    news = get_object_or_404(News, pk=pk)
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
    form = SimpleForm()
    context = {'form': form, 'title': 'Simple Form','category':category}
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newssummary = request.POST.get('newssummary')
        newsbody = request.POST.get('body')
        newsid = request.POST.get('newscategory')
        newstags = request.POST.get('newstags')
#       print(newstitle," ",newscategory," ",newssummary," ",newsbody)
        if newstitle == "" or newssummary == "" or newsbody==None or newscategory == "":
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
                    counting_cat_id = SubCategory.objects.get(pk=newsid).category_id
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
                show=0,
                counting_cat_id=counting_cat_id
                )
                    news_added.save()
                    count = len(News.objects.filter(counting_cat_id=counting_cat_id))

                    category_count = Category.objects.get(pk=counting_cat_id)
                    category_count.count = count
                    category_count.save()
                    return redirect('news_list')
                else:
                    error: "Your file is bigger than 5 Mb"
                    return render(request,'back/error.html',{'error':error})
            
            else:
                error = "Your file not supported"
                return render(request,'back/error.html',{'error':error})

        except:
            fs = FileSystemStorage()
            fs.delete(filename)
            error = "Please input your image"
            print(newstags, newsbody, newscategory, newsid, url, newstags, filename, newsname,time, today, myfile)
            return render(request,'back/error.html',{'error':error})
    
    return render(request, 'back/news_add.html',context)

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
    form = PostForm(some_body=news.body)
    context = {'form':form, 'title': 'Simple Form','category':category}

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        newssummary = request.POST.get('newssummary')
        newsbody = request.POST.get('body')
        newsid = request.POST.get('newscategory')
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
    return render(request, 'back/news_edit.html',{'pk':pk,'news':news,'category':category,'form': form, 'title': 'Simple Form'})


def markdown_uploader(request):
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))

