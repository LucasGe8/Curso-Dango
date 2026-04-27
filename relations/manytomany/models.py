from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=200)
    publications = models.ManyToManyField(Publication)
    
    def __str__(self):
        return self.headline
