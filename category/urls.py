
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^panel/category/list/$',views.category_list, name='category_list'),
    url(r'^panel/category/add/$',views.category_add, name='category_add'),
    url(r'^panel/category/delete/(?P<pk>\d+)/$',views.category_delete, name='category_delete'),
]