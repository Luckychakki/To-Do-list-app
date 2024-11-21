from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

# Create your views here.
def task_list(request):
    try:
        tasks = Task.objects.all()
        form = TaskForm()
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("task-list")
        return render(request, "task_list.html", {"tasks": tasks, "form": form})
    except Exception as e:
        print(e)
        return HttpResponse("Error")



def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    return render(request, "task_list.html", {"form": form})


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("task-list")
    return render(request, "task_delete.html", {"task": task})