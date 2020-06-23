from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from news.models import News

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        News.body: {'widget': AdminMartorWidget},
    }

admin.site.register(News, YourModelAdmin)