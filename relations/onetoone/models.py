from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    number_of_employees = models.IntegerField()
    
    def __str__(self):
        return self.place.name