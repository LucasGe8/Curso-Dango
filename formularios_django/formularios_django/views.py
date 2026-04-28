from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

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

def widget(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, "widget.html", {"form": form}) 
        
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #Aquí van todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("<h1>Formulario enviado correctamente</h1>")
        else:
            #Aquí van todas las acciones a realizar cuando los datos son incorrectos    
            return render(request, "widget.html", {"form": form}) 
        return render(request, "widget.html", {"form": form}) 


    
