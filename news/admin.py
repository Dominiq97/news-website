from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from .models import News
from django.db import models

admin.site.register(News, MarkdownxModelAdmin)

