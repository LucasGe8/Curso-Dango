from django.http import HttpResponse
from django.shortcuts import render
from stock.forms import ProductForm

def index(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Producto guardado correctamente</h1>")
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})
