# Luminary_registration\models.py
from django.db import models
from django.contrib.auth.models import User


class LuminaryWriter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )

    def __str__(self):
        return self.user.username
