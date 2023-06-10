from django.urls import path
from .views import UserCreateView, TaskCreateView, TaskReadView, TaskUpdateView, TaskDeleteView
from django.contrib.auth.decorators import login_required

app_name = "tasks"

urlpatterns = [
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("user/<int:user_id>/task/create/", login_required(TaskCreateView.as_view()), name="task-create"),
    path("user/<int:user_id>/task/<int:task_id>/", login_required(TaskUpdateView.as_view()), name="task-update"),
    path("user/<int:user_id>/task/delete/<int:task_id>/", login_required(TaskDeleteView.as_view()), name="task-delete"),
    path("user/<int:user_id>/task/list/", login_required(TaskReadView.as_view()), name="task-list")
]
