from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django import template
from django.conf import settings
import markdown2
import bleach

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    body = MarkdownxField()
    date = models.CharField(max_length=12,default="//")
    time = models.CharField(max_length=12,default="00:00") 
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="-")
    category_id = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    @property 
    def formatted_markdown(self):  # <--- We'll need this for views.py later
        return markdownify(self.body)

    def __str__(self):
        return self.name