from django.shortcuts import render
from .models import Task, SubTask, Note, Category, Priority

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'taskmanager/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    subtasks = task.subtask_set.all()
    notes = task.note_set.all()
    return render(request, 'taskmanager/task_detail.html', {
        'task': task, 'subtasks': subtasks, 'notes': notes
    })

def dashboard(request):
    total = Task.objects.count()
    completed = Task.objects.filter(status='Completed').count()
    pending = Task.objects.filter(status='Pending').count()
    in_progress = Task.objects.filter(status='In Progress').count()
    recent_tasks = Task.objects.all().order_by('-created_at')[:5]
    return render(request, 'taskmanager/dashboard.html', {
        'total': total,
        'completed': completed,
        'pending': pending,
        'in_progress': in_progress,
        'recent_tasks': recent_tasks,
    })