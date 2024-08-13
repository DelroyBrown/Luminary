# Luminary_base\urls.py
from django.contrib import admin
from django.urls import path, include

app_name = "Luminary_base"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Luminary_home.urls")),
    path("", include("Luminary_registration.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("Luminary_writers.urls")),
]
