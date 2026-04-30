from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_task(request):
    return render(request, 'new.html')

def edit_task(request, task_id):
    return render(request, 'edit.html')

def delete_task(request, task_id):
    return render(request, 'delete.html')