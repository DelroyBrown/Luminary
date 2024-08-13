# Luminary_registration\views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LuminaryRegistrationForm


def register(request):
    if request.method == "POST":
        form = LuminaryRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Luminary_home:home")
    else:
        form = LuminaryRegistrationForm()

    return render(request, "registration/register.html", {"form": form})
