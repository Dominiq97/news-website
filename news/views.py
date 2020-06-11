from django.shortcuts import render
from .models import News
from main.models import Main

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
        print(newstitle," ",newscategory," ",newssummary," ",newsbody)
    return render(request, 'back/news_add.html')


