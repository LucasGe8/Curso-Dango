from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tasks'),
    path('create', views.create_task, name='create_task'),
    path('edit/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
]