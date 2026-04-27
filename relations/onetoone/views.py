from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create(request):
    lugar = Place(
        name="Residencia Vibe",
        address="Detrás de la Catedral"
    )
    restaurante = Restaurant(
        place=lugar,
        number_of_employees=10
    )
    lugar.save()
    restaurante.save()
    return HttpResponse(restaurante.place.name)