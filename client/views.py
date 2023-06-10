from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms_user import UserForm
from .forms_tasks import TaskForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models_user import UserProfile
from django.contrib import messages
from django.db.models import Q
from .model_tasks import Tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class UserCreateView(CreateView):
    template_name = "client/user.html"
    form_class = UserForm
    success_url = reverse_lazy("tasks:user-create")

    def form_valid(self, form):

        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        birth_date = form.cleaned_data['birth_date']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name, birth_date=birth_date,
                                   email=email)

        return redirect("index")


class TaskCreateView(CreateView):
    template_name = "client/task.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-create")

    def form_valid(self, form):
        try:
            task = form.save(commit=False)
            task.user_id = User.objects.get(id=self.request.user.id)
        except Exception:
            messages.error("Error to save your task.")
            print(Exception)
        else:
            task.save()
        return redirect("index")


class TaskReadView(LoginRequiredMixin, ListView):
    template_name = "client/task_list.html"
    paginate_by = 10
    model = Tasks

    def get_queryset(self):
        title = self.request.GET.get('title')
        user = self.request.user
        if title:
            object_list = self.model.objects.filter(
                Q(title__icontains=title) | Q(tags__icontains=title)
            )
        else:
            object_list = self.model.objects.filter(user_id=user)
        return object_list.order_by('date_creation_task')


class TaskUpdateView(UpdateView):
    template_name = "client/task.html"
    model = Tasks
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-create")

    def get_object(self):
        task_id = self.kwargs.get("task_id")
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(Tasks, user_id=user_id, id=task_id)

    def form_valid(self, form):
        try:
            task = form.save(commit=False)
            task.user_id = User.objects.get(id=self.request.user.id)
        except Exception:
            messages.error("Error to save your task.")
            print(Exception)
        else:
            task.save()
        return redirect("index")


class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = "tasks:task-list"

    def get_object(self):
        task_id = self.kwargs.get("task_id")
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(Tasks, user_id=user_id, id=task_id)

    def get_success_url(self):
        user_id = self.kwargs.get("user_id")
        return reverse_lazy("tasks:task-list", kwargs={"user_id": user_id})
