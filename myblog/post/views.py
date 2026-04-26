from django.shortcuts import render, HttpResponse
from .models import Entry, Author
# Create your views here.

def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all()
    entries = Entry.objects.all()
    
    #Datos filtrados por condición 
    filtered = Author.objects.filter(email='natashahood@example.net')
    
    #Obtener un objeto especifico
    specific = Author.objects.get(id=1)
    
    #Limitación de busqueda, en este caso los primeros 10 objetos
    limit = Author.objects.all()[:10]
    
    #Obtener los valores en un rango, en este caso desde el 5 hasta el 10
    offsets = Author.objects.all()[5:10]
    return render(request,'post/queries.html',{'authors': authors, 'entries': entries, 'filtered': filtered, 'specific': specific, 'limit': limit, 'offsets': offsets})