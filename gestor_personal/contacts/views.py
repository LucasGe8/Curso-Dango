from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from .models import Contact

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contact/index.html", {'contacts': contacts})

def create_contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact.is_valid():
            contact.save()
            return redirect('contacts')
    return render(request, "contacts.html", {'contact': contact})

def edit_contact(request, id):
    contact = ContactForm(request.POST or None, instance=Contact.objects.get(id=id))
    if request.method == 'POST':
        if contact.is_valid():
            contact.save()
            return redirect('contacts')
    return render(request, "contacts.html", {'contact': contact})

def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contacts')

