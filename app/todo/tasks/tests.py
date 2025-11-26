from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskCRUDTests(TestCase):

    def setUp(self):
        """
        Set up a sample task that can be used by all test methods.
        """
        self.task = Task.objects.create(
            name='Initial Test Task',
            comment='A comment for the initial task.',
            status=Task.Status.PENDING
        )

    def test_task_list_view(self):
        """
        Test that the task list view loads correctly and displays the task.
        """
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Initial Test Task')
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_task_create_view(self):
        """
        Test that a new task can be created.
        """
        # Test that the create page loads
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')

        # Test submitting a new task
        new_task_data = {
            'name': 'New Task from Test',
            'comment': 'This is a new task.',
            'status': Task.Status.PENDING
        }
        response = self.client.post(reverse('task-create'), new_task_data)

        # Should redirect to the task list on success
        self.assertRedirects(response, reverse('tasks'))

        # Verify the task was created in the database
        self.assertTrue(Task.objects.filter(name='New Task from Test').exists())

    def test_task_update_view(self):
        """
        Test that an existing task can be updated.
        """
        update_url = reverse('task-update', args=[self.task.pk])

        # Test that the edit page loads
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')

        # Test submitting updated data
        updated_data = {
            'name': 'Updated Test Task',
            'comment': 'The comment has been updated.',
            'status': Task.Status.DONE,
        }
        response = self.client.post(update_url, updated_data)
        self.assertRedirects(response, reverse('tasks'))

        # Verify the task was updated in the database
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Test Task')
        self.assertEqual(self.task.status, Task.Status.DONE)

    def test_task_delete_view(self):
        """Test that a task can be deleted."""
        delete_url = reverse('task-delete', args=[self.task.pk])
        response = self.client.post(delete_url)
        self.assertRedirects(response, reverse('tasks'))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
