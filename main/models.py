from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=60)
    about = models.TextField()
    fb = models.CharField(default="-",max_length=30)
    tw = models.CharField(default="-",max_length=30)
    yt = models.CharField(default="-",max_length=30)
    tel = models.CharField(default="-",max_length=30)
    link = models.CharField(default="-",max_length=30)
    set_name = models.CharField(default="-",max_length=30)

    def __str__(self):
        return self.set_name + " | " + str(self.pk)

    class Meta:
        verbose_name_plural = 'Main Characteristics'
    
    


