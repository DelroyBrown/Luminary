# Luminary_essays\models.py
from django.db import models
from tinymce.models import HTMLField
from Luminary_registration.models import LuminaryWriter


class EssayCategory(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False, default='')

    def __str__(self):
        return self.name


class Essay(models.Model):
    luminary_writer = models.ForeignKey(
        LuminaryWriter, on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=200)
    essay_category = models.ForeignKey(EssayCategory, on_delete=models.CASCADE)
    content = HTMLField(blank=False, null=False, default="")
    blockquote = models.TextField(blank=False, null=False, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    audio_file = models.FileField(upload_to="audio", blank=True, null=True)
    image = models.ImageField(upload_to='essay-images', blank=False, null=False)

    def __str__(self):
        return self.title
