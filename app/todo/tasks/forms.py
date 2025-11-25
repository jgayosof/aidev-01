from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    A form for creating and updating Task objects.
    """
    class Meta:
        model = Task
        fields = ['name', 'comment', 'status']