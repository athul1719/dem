from django.db import models

# Create your models here.

class destination(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')
    desc=models.TextField()
    def __str__(self):
        return self.name

class names(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name