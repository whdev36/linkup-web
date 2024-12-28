from django.db import models
from django.contrib.auth.models import AbstractUser
# from config.settings import AUTH_USER_MODEL

# Profile
class Profile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/users/', blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    follows = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
    profile_video = models.FileField(upload_to='profiles/videos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or self.username
        super().save(*args, **kwargs)

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile, related_name="liked_posts", blank=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"

    @property
    def like_count(self):
        return self.likes.count()
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username} at {self.timestamp}"
