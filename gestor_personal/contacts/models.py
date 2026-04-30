from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=15, blank=False, null=False)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, blank=False, null=False)
    
    def __str__(self):
        return self.name + " " + self.last_name