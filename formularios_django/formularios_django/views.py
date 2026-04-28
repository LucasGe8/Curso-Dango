from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm

def form(request):
    comment_form = CommentForm()
    return render(request, "form.html", {"comment_form": comment_form})

def goal(request):
    if request.method != "POST":
        return HttpResponse("<h1>No se permiten peticiones GET</h1>")
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        nombre = request.POST.get("nombre")
        comentario = request.POST.get("comentario")
        url = request.POST.get("url")   
        return render(request, "goal.html", {"nombre": nombre, "comentario": comentario, "url": url})
        