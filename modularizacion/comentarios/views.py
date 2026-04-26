from django.shortcuts import render, HttpResponse
from .models import Comentario

# Create your views here.

def test(request):
    return HttpResponse("<h1>Hola desde Comentarios</h1>")
def create(request):
    
    #comentario = Comentario(
    #    nombre = "Lucas",
    #    score = 10,
    #    comentario = "Hola, este es un comentario de prueba"
    #)
    #comentario.save()
    comentario = Comentario.objects.create(nombre="Lucas", score=5, comentario="Probando create")
    return HttpResponse("<h1>Creando comentarios</h1>")

def delete(request, id):
    #comentario = Comentario.objects.get(id=id)
    #comentario.delete()
    comentario = Comentario.objects.filter(id=id).delete()
    return HttpResponse("<h1>Comentario eliminado</h1>")