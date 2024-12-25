from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    instagram_username = models.CharField(max_length=120, blank=True, null=True)
    telegram_username = models.CharField(max_length=120, blank=True, null=True)
    facebook_username = models.CharField(max_length=120, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='accounts/pics/', blank=True, null=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.username