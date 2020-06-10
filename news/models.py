from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    body = models.TextField()
    date = models.CharField(max_length=12,default="//")
    pic = models.TextField()
    writer = models.CharField(max_length=50)

    def __str__(self):
        return self.name