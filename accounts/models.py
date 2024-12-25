from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re

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

    # Custom method to get all social media usernames
    def get_social_media_links(self):
        social_links = {}
        if self.instagram_username:
            social_links['Instagram'] = f'https://www.instagram.com/{self.instagram_username}'
        if self.telegram_username:
            social_links['Telegram'] = f'https://t.me/{self.telegram_username}'
        if self.facebook_username:
            social_links['Facebook'] = f'https://www.facebook.com/{self.facebook_username}'
        if self.website_url:
            social_links['Website'] = self.website_url
        return social_links

    # Clean method to validate Instagram, Telegram, and Facebook usernames format
    def clean(self):
        if self.instagram_username and not re.match(r'^[a-zA-Z0-9_.]+$', self.instagram_username):
            raise ValidationError({'instagram_username': 'Instagram username can only contain letters, numbers, underscores, and periods.'})
        if self.telegram_username and not re.match(r'^[a-zA-Z0-9_]+$', self.telegram_username):
            raise ValidationError({'telegram_username': 'Telegram username can only contain letters, numbers, and underscores.'})
        if self.facebook_username and not re.match(r'^[a-zA-Z0-9.]+$', self.facebook_username):
            raise ValidationError({'facebook_username': 'Facebook username can only contain letters, numbers, and periods.'})

    # Custom method to check if the profile is complete
    def is_profile_complete(self):
        return bool(self.first_name and self.last_name and self.profile_picture)

