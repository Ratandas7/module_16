from django.shortcuts import render, redirect
from tasks . forms import TaskForm
from tasks . models import Task
# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = TaskForm()
    return render(request, './tasks/add_task.html', {'form' : task_form})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request, './tasks/add_task.html', {'form' : task_form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
