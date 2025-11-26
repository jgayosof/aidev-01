from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/task_form.html'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/task_form.html'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
