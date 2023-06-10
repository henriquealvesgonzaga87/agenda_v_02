from django import forms
from .models_user import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = "date"


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateField(widget=DateInput())
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "username",
            "password1",
            "password2"
        )
