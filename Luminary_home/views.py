from django.shortcuts import render
from Luminary_essays.models import Essay


def home(request):
    recent_essays = Essay.objects.order_by("-created_at")[:1]
    return render(request, "home/home.html", {"recent_essays": recent_essays})
