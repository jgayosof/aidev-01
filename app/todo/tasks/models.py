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


class Task(BaseModel):
    """
    Represents a single task in the to-do list.
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        DONE = 'DONE', 'Done'
        CANCELLED = 'CANCELLED', 'Cancelled'

    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return self.name
