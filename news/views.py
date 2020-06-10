from django.shortcuts import render
from .models import News

# Create your views here.

def news_detail(request,pk):
    news = News.objects.filter(pk=pk)
    return render(request, 'front/news_detail.html',{'news':news})


