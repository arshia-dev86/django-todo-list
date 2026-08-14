from django.db import models

# Create your models here.

class Task(models.Model):
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