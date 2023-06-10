from django.contrib import admin
from .model_tasks import Tasks
from .models_user import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birth_date", "email"]


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ["title", "tags", "description", "task_date", "active"]
