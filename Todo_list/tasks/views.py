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
        deadline=request.POST.get('deadline') or None

        Task.objects.create(
                    title=title,
                    description=description,
                    priority=priority,
                    done=done,
                    deadline=deadline
                )

        return redirect('tasks')


    return render(request, 'tasks/add_task.html')

def delete_task(request, task_id):

    if request.method == 'POST':
        task= get_object_or_404(Task , id=task_id)
        task.delete()
        return redirect('tasks') 
           
    return render(request, 'tasks/delete_task.html', {'task': task})

def edit_task(request, task_id):
    if request.method == 'POST':

        task= get_object_or_404(Task, id=task_id)


        task.title= request.POST.get('title')
        task.description= request.POST.get('description')
        task.priority= request.POST.get('priority')
        task.done = "done" in request.POST
        deadline = request.POST.get('deadline') or None
        task.deadline= deadline

        task.save()

        return redirect("tasks")
    return render(request, 'tasks/edit_task.html', {'task': task})




def complete_task(request, task_id):
    if request.method == 'POST' :
        task = get_object_or_404(Task, id=task_id)
        task.done = True
        task.save()
    return redirect('tasks')