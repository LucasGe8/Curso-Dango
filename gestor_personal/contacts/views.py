from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact

@login_required
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contact/index.html", {'contacts': contacts})

@login_required
def create_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contacts')
    return render(request, "contact/contactform.html", {'form': form})

@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contacts')
    return render(request, "contact/contactform.html", {'form': form, 'contact': contact})

@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contacts')
