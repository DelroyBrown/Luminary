# Luminary_home\urls.py
from django.urls import path
from . import views

app_name = "Luminary_home"

urlpatterns = [
    path("", views.home, name="home"),
]
