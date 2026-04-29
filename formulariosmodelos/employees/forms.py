from django.forms import ModelForm
from django import forms
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        #exclude = ['email'] para excluir un campo
        #widgets = para modificar la apriencia de los campos y que se vean como Bootstrap
        #extra_fields = para agregar campos que no estan en el modelo
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }   
        