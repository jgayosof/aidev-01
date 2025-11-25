from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    An abstract base model that provides common fields for other models.
    - created_date: Automatically set when the object is first created.
    - modified_date: Automatically updated every time the object is saved.
    - active: A boolean to allow soft deletes.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Status(BaseModel):
    """
    Represents the status of a task (e.g., 'To Do', 'In Progress', 'Done').
    """
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("DONE", "Done"),
        ("CANCELLED", "Cancelled"),
    ]

    name = models.CharField(max_length=50,
                            unique=True,
                            choices=STATUS_CHOICES,
                            default="PENDING")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Task(BaseModel):
    """
    Represents a single task in the to-do list.
    """
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status,
                               on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
