
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
]