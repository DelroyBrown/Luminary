from django.shortcuts import render
from Luminary_essays.models import Essay
from Luminary_registration.models import LuminaryWriter


def writer_detail(request, username):
    luminary_writer = LuminaryWriter.objects.get(user__username=username)
    essays = Essay.post_set.all()
    return render(
        request,
        "luminary_writers/writer_detail.html",
        {"luminary_writer": luminary_writer, "essays": essays},
    )
