from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='accounts/pics/', blank=True, null=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.username