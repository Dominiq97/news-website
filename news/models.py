from django.db import models
from martor.models import MartorField


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    body = MartorField()
    date = models.CharField(max_length=12,default="//")
    time = models.CharField(max_length=12,default="00:00") 
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="-")
    category_id = models.IntegerField(default=0)
    show = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'News'

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'