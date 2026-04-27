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
    
    #Equivalente a Order by 
    ordered = Author.objects.order_by('nombre')
    
    #Obtener todos los elementos cuyo id sea menor o igual a 15
    rango_de_id = Author.objects.filter(id__lte=15)
    
    #Obtener todos los elementos que contengan en el nombre la palabra yes
    contiene_yes = Author.objects.filter(nombre__contains='Democratic')
    
    return render(request,'post/queries.html',{'authors': authors, 'entries': entries, 'filtered': filtered, 'specific': specific, 'limit': limit, 'offsets': offsets, 'ordered': ordered, 'rango_de_id': rango_de_id, 'contiene_yes': contiene_yes})