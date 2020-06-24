
from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
    url(r'^panel/news/list/$', views.news_list, name='news_list'),
    url(r'^panel/news/add/$', views.news_add, name='news_add'),
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),
    path('news_by/<str:tag>', views.ListNewsByTag.as_view(),name='list_by_tag'),
]