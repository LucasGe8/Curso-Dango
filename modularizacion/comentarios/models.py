from django.db import models
# Create your models here.

class Comentario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre", null = False, blank=False)
    score = models.IntegerField(default=3, verbose_name="Score")
    comentario = models.TextField(verbose_name="Comentario", null = False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True,verbose_name="Fecha", null = True)
    firma = models.CharField(max_length=100, verbose_name="Firma", default = 'Firma', blank=False)
    def __str__(self):
        return self.nombre


