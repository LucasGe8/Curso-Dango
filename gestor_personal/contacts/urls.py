from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('create/', views.create_contact, name='create_contact'),
    path('edit/<int:contact_id>', views.edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>', views.delete_contact, name='delete_contact')
]