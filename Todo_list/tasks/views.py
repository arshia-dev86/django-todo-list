from django.shortcuts import render, redirect, get_object_or_404
from .models import Task 
# Create your views here.

def show_tasks(request):
    tasks= Task.objects.all()
    return render(request, 'tasks/show_tasks.html', {'tasks' : tasks})


def add_task(request):
    if request.method == 'POST':

        title= request.POST.get('title')
        description= request.POST.get('description')
        done= request.POST.get('done') == 'on'
        priority= request.POST.get('priority')

        Task.objects.create(
                    title=title,
                    description=description,
                    priority=priority,
                    done=done
                )

        return redirect('tasks')


    return render(request, 'tasks/add_task.html')

def delete_task(request, task_id):
    task= get_object_or_404(Task , id=task_id)         
    return render(request, 'tasks/delete_task.html', {'task': task})
