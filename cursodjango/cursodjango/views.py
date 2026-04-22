from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html')

def dinamico(request,nombre):
    categorias = ['Materia','Ingenieria de Software','Programacion','Bases de datos','Redes']
    contexto={
        'nombre':nombre,
        'categorias':categorias
    }
    return render(request, 'dinamico.html', contexto)

def estaticos(request):
    return render(request, 'estaticos.html')

def herencia(request):
    return render(request, 'herencia.html')

def inclusion(request):
    return render(request, 'inclusion.html')

def otra(request):
    return render(request, 'otra.html')

def index(request):
    return render(request, 'index.html')
