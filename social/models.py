from django.db import models
from django.contrib.auth.models import AbstractUser
# from config.settings import AUTH_USER_MODEL

# Profile
class Profile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/users/', blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    follows = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.username
        super().save(*args, **kwargs)
