from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^panel/subcategory/list/$',views.subcategory_list, name='subcategory_list'),
    url(r'^panel/subcategory/add/$',views.subcategory_add, name='subcategory_add'),
    url(r'^panel/subcategory/delete/(?P<pk>\d+)/$',views.subcategory_delete, name='subcategory_delete'),
    url(r'^panel/subcategory/edit/(?P<pk>\d+)/$',views.subcategory_edit, name='subcategory_edit'),
]