from django.http import HttpResponse
from django.shortcuts import render


def getform(request):
    return render(request, "forms.html")

def getgoal(request):
    if request.method != "GET":
        return HttpResponse("<h1>Metodo POST utilizado</h1>")
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    comentario = request.GET.get("comentario")
    return render(request, "success.html", {"nombre": nombre, "apellido": apellido, "comentario": comentario})

def postform(request):
    return render(request, "postform.html")

def postgoal(request):
    if request.method != "POST":
        return HttpResponse("<h1>Metodo POST no utilizado</h1>")
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    comentario = request.POST.get("comentario")
    return render(request, "success.html", {"nombre": nombre, "apellido": apellido, "comentario": comentario})