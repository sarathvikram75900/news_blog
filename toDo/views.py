from django.shortcuts import render,redirect
from . models import Task
# Create your views here.
def index(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(is_completed=True)
    return render(request,'toDo/index.html',{'tasks':tasks,'completed_tasks':completed_tasks})

def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('index')
    else:
        return render(request,'toDo/index.html')
    

def mark_as_done(request,pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('index')

def mark_as_undone(request,pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('index')

def edit_task(request,pk):
    get_task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        new_task = request.POST['edit_task']
        get_task.task = new_task
        get_task.save()
        return redirect('index')
    else:
        return render(request,'toDo/edit_task.html',{'get_task':get_task})


def delete_task(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')