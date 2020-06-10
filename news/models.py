from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    body = models.TextField()
    name = models.CharField(max_length=12)
    pic = models.TextField()
    writer = models.CharField(max_length=50)

    def __str__(self):
        return self.name