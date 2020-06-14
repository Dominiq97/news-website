
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^panel/category/list/$',views.category_list, name='category_list'),
]