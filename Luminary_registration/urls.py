# Luminary_registration\urls.py
from django.urls import path
from . import views

app_name = "Luminary_registration"

urlpatterns = [
    path("register/", views.register, name="register"),
]
