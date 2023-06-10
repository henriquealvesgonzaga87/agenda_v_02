from django import forms
from .model_tasks import Tasks


class DateTimeForm(forms.TextInput):
    input_type = "datetime-local"


class TaskForm(forms.ModelForm):
    title = forms.CharField()
    tags = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    task_date = forms.DateTimeField(widget=DateTimeForm)

    class Meta:
        model = Tasks
        fields = (
            "title",
            "tags",
            "description",
            "task_date",
        )
