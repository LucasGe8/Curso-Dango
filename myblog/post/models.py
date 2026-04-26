from django.db import models

# Create your models here.
class Author(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.nombre

class Entry(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    def __str__(self):
        return self.titulo
    
