from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as app_login, logout as app_logout
from django.contrib import messages


def login(request):
    return render(request, "login.html")


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            app_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "User or password invalid. Please, try again!")
    else:
        if not request.user.is_authenticated:
            return redirect("user-create")
    return redirect("index")


def logout(request):
    app_logout(request)
    return redirect("login")


def check_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        return redirect("login")
