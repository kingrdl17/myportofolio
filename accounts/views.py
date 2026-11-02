from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import StyledAuthenticationForm, StyledUserCreationForm


def register(request):
    form = StyledUserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account successfully created, please login.")
        return redirect("accounts:login")

    return render(
        request,
        "pages/accounts/register.html",
        {"name": "Clay", "form": form},
    )


def login_user(request):
    form = StyledAuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("profiles:show_main")
        response.set_cookie("last_login", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return response

    return render(
        request,
        "pages/accounts/login.html",
        {"name": "Clay", "form": form},
    )


def logout_user(request):
    logout(request)
    response = redirect("profiles:show_main")
    response.delete_cookie("last_login")
    return response
