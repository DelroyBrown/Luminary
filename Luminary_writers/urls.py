# Luminary_writers\urls.py
from django.urls import path
from . import views

app_name = "Luminary_writers"

urlpatterns = [
    path("luminary-writer/<str:username>/", views.writer_detail, name="luminary_writer"),
]
