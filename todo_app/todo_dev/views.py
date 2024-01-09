from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect

from .forms import *
# class TaskListCreateView(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# views.py
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print("Form is not valid:", form.errors)

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo_dev/index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
   
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("Form not valid", form.errors)
        
    context = {'form':form}
    return render(request,'todo_dev/update_task.html', context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'todo_dev/delete.html', context)