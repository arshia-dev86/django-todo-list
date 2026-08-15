from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=75 , blank=False)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    done= models.BooleanField(default=False)
    priority= models.CharField(
        max_length=10,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
    default='medium'
    )
    deadline = models.DateTimeField(null=True, blank=True)