from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

#Listado de Tareas
@login_required
def index(request):
    tasks = Task.objects.all()
    return render(request, "task/index.html", {'tasks': tasks})

#-------------------------------------CRUD de Tareas----------------------------------------- 

@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tasks')
    return render(request, "task/taskform.html", {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tasks')
    return render(request, "task/taskform.html", {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')
# --------------------------------------------------------------------------------