from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Status
from .forms import TaskForm

# Create your views here.

def task_list(request):
    """
    A view to display a list of active tasks, ordered by creation date.
    """
    tasks = Task.objects.filter(active=True).order_by('created_date')
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/task_list.html', context)

def task_create(request):
    """
    A view to handle creating a new task.
    - GET: Displays an empty form.
    - POST: Validates and saves the new task, then redirects to the task list.
    """
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task-list')
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    """
    A view to handle updating an existing task.
    - GET: Displays a pre-filled form for the specified task.
    - POST: Validates and saves the changes, then redirects to the task list.
    """
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task-list')
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    """
    A view to handle deleting a task.
    - GET: Renders a confirmation page.
    - POST: Deletes the task and redirects to the task list.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
