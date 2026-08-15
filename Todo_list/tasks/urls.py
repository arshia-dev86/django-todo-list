from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks, name='tasks'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('login/', views.login_view ,name='login'),
    path('register/' , views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout' )
]
