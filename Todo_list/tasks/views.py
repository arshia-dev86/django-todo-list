from django.shortcuts import render
from .models import Task 
# Create your views here.

def show_tasks(request):
    tasks= Task.objects.all()
    return render(request, 'tasks/show_tasks.html', {'tasks' : tasks})