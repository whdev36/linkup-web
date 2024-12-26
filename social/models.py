from django.db import models
from django.contrib.auth.models import AbstractUser

# Profile
class Profile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/users/', blank=True, null=True)
    bio = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.username
        super().save(*args, **kwargs)
