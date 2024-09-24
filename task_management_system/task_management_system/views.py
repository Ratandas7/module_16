from django.shortcuts import render
from tasks . models import Task
def home(request):
    return render(request, 'home.html')

def show_task(request):
    task = Task.objects.all()
    # for i in task:
    #     print(i)
    #     for j in i.category.all():
    #         print(j)
    return render(request, 'show_task.html', {'data' : task})


