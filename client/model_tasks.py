from django.db import models
from .models_user import UserProfile, User
from django.urls import reverse


class Tasks(models.Model):
    title = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)
    description = models.TextField()
    task_date = models.DateField()
    date_creation_task = models.DateField(auto_now_add=True)
    date_update_task = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def get_input_date(self):
        return self.birth_date.strftime("%Y-%m-%dT%H:%M")

    def get_date_event(self):
        return self.task_date.strftime("%Y-%m-%dT%H:%M")

    def get_absolute_url(self):
        user_id = self.user_id
        task_id = self.id
        return reverse("tasks:task-update", kwargs={"user_id": user_id, "task_id": task_id})

    def get_delete_url(self):
        return reverse("tasks:task-delete", kwargs={"id": self.id})
