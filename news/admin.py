from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import News
from .models import Tag

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        News.body: {'widget': AdminMartorWidget},
    }

admin.site.register(News, YourModelAdmin)
admin.site.register(Tag)