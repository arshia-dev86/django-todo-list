from django.shortcuts import render, redirect, get_object_or_404
from .models import Task 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')

        if confirm_password != password : 
            return render(request, 'accounts/register.html', {'error' : 'Passwords do not match.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error' : 'This username is already taken.'})


        User.objects.create_user(username=username, password=password)
        return redirect("login")
    return render(request, 'accounts/register.html')




def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tasks")

        else:
            return render(request , 'accounts/login.html', {'error': 'Invalid username or password'})

    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    if request.method =='POST':
        logout(request)
    return redirect('login')


@login_required
def show_tasks(request):
    filter_type = request.GET.get('filter', 'all')

    if filter_type == 'active':
        tasks = Task.objects.filter(user=request.user, done=False)

    elif filter_type == 'completed':
        tasks = Task.objects.filter(user=request.user, done=True)

    else:
        tasks = Task.objects.filter(user=request.user)

    return render(request, 'tasks/show_tasks.html', {
        'tasks': tasks,
        'filter_type': filter_type
    })

@login_required
def add_task(request):
    if request.method == 'POST':

        user= request.user
        title= request.POST.get('title')
        description= request.POST.get('description')
        done= request.POST.get('done') == 'on'
        priority= request.POST.get('priority')
        deadline=request.POST.get('deadline') or None

        if deadline: 
            deadline = datetime.strptime( deadline, '%Y-%m-%dT%H:%M' ) 
            deadline = timezone.make_aware(deadline) 
            if deadline < timezone.now(): 
                return render( request, 'tasks/add_task.html', { 'error': 'Deadline cannot be in the past.' })

        Task.objects.create(
                    user=user,
                    title=title,
                    description=description,
                    priority=priority,
                    done=done,
                    deadline=deadline
                )

        return redirect('tasks')


    return render(request, 'tasks/add_task.html')

@login_required
def delete_task(request, task_id):
    task= get_object_or_404(Task , id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks') 
           
    return render(request, 'tasks/delete_task.html', {'task': task})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        done = request.POST.get('done') == 'on'
        deadline = request.POST.get('deadline') or None

        if deadline:
            deadline = datetime.strptime(deadline,'%Y-%m-%dT%H:%M')

            deadline = timezone.make_aware(deadline)

            if deadline < timezone.now():
                return render(request,'tasks/edit_task.html',{'task': task,'error': 'Deadline cannot be in the past.'})

        task.title = title
        task.description = description
        task.priority = priority
        task.done = done
        task.deadline = deadline

        task.save()

        return redirect('tasks')

    return render(request,'tasks/edit_task.html',{'task': task})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST' :
        task.done = True
        task.save()
    return redirect('tasks')